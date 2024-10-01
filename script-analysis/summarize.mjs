
import fs from 'fs';

let json = fs.readFileSync('agent-perf.json', 'utf-8');

json = json.split('\n').slice(0, -1).map(JSON.parse);

let lastRequests = 0;

for (let i = 0; i < json.length; i++) {
  let { timestamp, requests, prefix, measurements } = json[i];

  if (prefix !== 'patcher') {
    console.log(`skipping ${timestamp} not patcher`);
    continue;
  }

  if (requests === lastRequests) {
    console.log(`skipping ${timestamp} no new requests`);
    continue;
  }
  lastRequests = requests;

  const prefixLen = prefix.length + 1;
  const runOrig = ':native:runOriginalFunction';
  const runOrigLen = runOrig.length;
  const wrapper = ':wrapper';
  const wrapperLen = wrapper.length;

  const summarized = [];
  const unified = {};
  for (const measurement of measurements) {
    const { tag, n, totalMicros, mean } = measurement;
    if (tag.endsWith(runOrig)) {
      const unifiedTag = tag.slice(prefixLen, -runOrigLen);
      if (unifiedTag in unified) {
        throw new Error(`wrapper came first1 ${timestamp} ${unifiedTag}`);
        // merge, but this should never happen because the native
        // function should always complete before the wrapper.
      } else {
        unified[unifiedTag] = { tag: unifiedTag, n, nativeMicros: totalMicros, nativeMean: mean };
      }
    } else if (tag.endsWith(wrapper)) {
      const unifiedTag = tag.slice(prefixLen, -wrapperLen);
      if (unifiedTag in unified) {
        unified[unifiedTag].wrapperMicros = totalMicros;
        unified[unifiedTag].wrapperMean = mean;

        const ratio = totalMicros / unified[unifiedTag].nativeMicros;
        const delta = totalMicros - unified[unifiedTag].nativeMicros;

        unified[unifiedTag].ratio = ratio;
        unified[unifiedTag].delta = delta;

        summarized.push(unified[unifiedTag]);
      } else {
        throw new Error(`wrapper came first2 ${timestamp} ${unifiedTag}`);
        // this should never happen either.
        unified[unifiedTag] = { n, wrapperMicros: totalMicros, wrapperMean: mean };
      }
    }
  }

  if (summarized.length) {
    if (process.env.SORT === 'delta') {
      summarized.sort(sortDelta);
    } else if (process.env.SORT === 'ratio') {
      summarized.sort(sortRatio);
    } else if (process.env.SORT === 'deltaPer') {
      summarized.sort(sortDeltaPer);
    }
    //summarized.sort((a, b) => compare(a.ratio, b.ratio));
    console.log(`\n${timestamp}`);
    for (const { tag, n, nativeMicros, nativeMean, wrapperMicros, wrapperMean, ratio, delta } of summarized) {
      console.log(`${tag} ${n} ratio ${f2(ratio)} delta ${f2(delta)} deltaPer ${f2(delta / n)}`);

      // console.log(`${tag} ${n} ${f2(nativeMicros)} ${f2(nativeMean)} ${f2(wrapperMicros)} ${f2(wrapperMean)} ${f2(ratio)} ${f2(delta)}`);
    }
    break;
  }

}

function f2(x) {
  return x.toFixed(2);
}

function sortRatio(a, b) {
  return b.ratio - a.ratio;
}

function sortDelta(a, b) {
  return b.delta - a.delta;
}

function sortDeltaPer(a, b) {
  return b.delta / b.n - a.delta / a.n;
}
