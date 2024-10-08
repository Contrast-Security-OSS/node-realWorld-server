
import fs from 'fs';

//
// the only command line option is to supply the filename.
//
// this is a work in progress.
//
// definitions:
// - wrapper - the code that the agent wraps a patched function with
// - original - the code that the agent is wrapping, e.g., String.prototype.concat
// - delta - the total difference, for all invocations, between the time taken
// to execute the wrapper and the time taken to execute the original
// - deltaPer - delta divided by number of invocations
// - ratio - the ratio of the wrapper time to the original time.
//
// set env var SORT to `delta`, `ratio`, or `deltaPer` to sort the output
// set env var VERBOSE to 1 to see skipped items.
//
const verbose = process.env.VERBOSE === '1';

const filename = process.argv[2] || 'agent-perf.jsonl';

let json = fs.readFileSync(filename, 'utf-8');

json = json.split('\n').slice(0, -1).map(JSON.parse);

let lastRequests = 0;

for (let i = 0; i < json.length; i++) {
  let { timestamp, requests, prefix, measurements } = json[i];

  if (process.env.STATS === 'reporter' || process.env.STATS === 'contrast-ui-reporter') {
    if (prefix !== 'contrast-ui-reporter') {
      verbose && console.log(`skipping ${timestamp} not reporter`);
      continue;
    }
  }
  else if (prefix !== 'patcher') {
    verbose && console.log(`skipping ${timestamp} not patcher`);
    continue;
  }

  if (requests === lastRequests) {
    verbose && console.log(`skipping ${timestamp} no new requests`);
    continue;
  }
  lastRequests = requests;

  const prefixLen = prefix.length + 1;
  const runOrig = ':native:runOriginalFunction';
  const runOrigLen = runOrig.length;
  const wrapper = ':wrapper';
  const wrapperLen = wrapper.length;
  const post = ':post';
  const postLen = post.length;

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
    } else if (tag.endsWith(post)) {
      const unifiedTag = tag.slice(prefixLen, -postLen);

      unified[unifiedTag] = { n, wrapperMicros: totalMicros, wrapperMean: mean };
      unified[unifiedTag].tag = unifiedTag;

      summarized.push(unified[unifiedTag]);
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

    let deltaPerReq = 0;

    console.log(`\n${timestamp}`);
    for (const { tag, n, nativeMicros, nativeMean, wrapperMicros, wrapperMean, ratio, delta } of summarized) {
      const raw = `(raw w ${wrapperMean}, o ${nativeMean})`;
      if (ratio) {
        console.log(`${tag} ${n} ratio ${f2(ratio)} delta ${f2(delta)} deltaPer ${f2(delta / n)} ${raw}`);
      } else {
        const raw = `(raw w ${wrapperMean}, total ${wrapperMicros})`;
        console.log(`${tag} ${n} ${raw}`);
      }
      // total number of invocations / requests => invocations/request
      // invocations/request * deltaPer => deltaPerReq
      const deltaPer = delta / n;
      deltaPerReq += (n / requests) * deltaPer;
      // console.log(`${tag} ${n} ${f2(nativeMicros)} ${f2(nativeMean)} ${f2(wrapperMicros)} ${f2(wrapperMean)} ${f2(ratio)} ${f2(delta)}`);
    }

    if (deltaPerReq) console.log(`deltaPerReq ${f2(deltaPerReq)}`);

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
