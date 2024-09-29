from data import _useq

# https://www.lipsum.com/

# known as slug to the application...
titles = [
    "Nullam at mauris maximus libero",
    "Proin accumsan semper odio et",
    "In ullamcorper facilisis ante, id",
    "Nam sodales viverra ante at",
    "Interdum et malesuada fames ac",
]

descriptions = [
    "Mauris nec suscipit",
    "Neque fusce hendrerit",
    "Ligula vitae vestibulum",
    "Rutrum leo erat",
    "Rutrum urna eu"
]

tags = [
    "integer",
    "mattis",
    "orci",
    "placerat",
    "hendrerit",
]

lorem01 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eu tellus lorem. Nulla laoreet semper ligula sit amet consequat. Sed elementum, quam sit amet porttitor suscipit, dui leo porttitor justo, sodales congue tortor justo nec urna. In ac lorem non massa elementum blandit. Sed lobortis urna eu ipsum porta aliquam. Phasellus ullamcorper, nibh ut pretium iaculis, odio justo placerat mauris, a imperdiet lectus urna commodo lectus. Etiam mattis tempor augue, eget vulputate justo luctus at. Praesent varius et leo et fermentum. Sed rutrum a augue a luctus. Vestibulum vitae eros nisl. In convallis porttitor euismod. Phasellus a nisi sit amet enim venenatis laoreet vel sit amet urna. Curabitur faucibus, elit in rutrum pharetra, eros mauris dapibus justo, id ullamcorper urna sapien eu dolor. Suspendisse potenti.
"""

lorem02 = """Duis ex enim, dictum id purus non, venenatis convallis lacus. Praesent in rhoncus leo. Donec egestas dolor libero. Nulla gravida sit amet nisl in convallis. Duis porttitor laoreet posuere. Nullam sit amet metus et mi bibendum tristique. Integer dignissim placerat orci vitae tincidunt. Etiam viverra ornare urna, eget lobortis quam lacinia eu. Maecenas rhoncus, mi quis iaculis placerat, ipsum ligula aliquam nisl, et efficitur nulla leo nec velit. Nulla suscipit libero id commodo laoreet. Ut et nibh auctor, iaculis felis ac, maximus turpis. Proin faucibus viverra venenatis. Curabitur augue lacus, mollis quis eleifend in, mollis non dolor. Quisque venenatis ex eget volutpat elementum.
Quisque id felis magna. Aenean sed tempus felis, eget ultricies nulla. Nam gravida turpis ac neque pellentesque aliquam vitae sed massa. Morbi tincidunt cursus elit, eget blandit nunc cursus a. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam at pretium est, vitae molestie tellus. Fusce sollicitudin, diam sed efficitur aliquet, turpis ante posuere odio, non molestie tellus libero in odio. Suspendisse potenti. Etiam ut finibus sem. Mauris suscipit hendrerit sem sed fermentum. Mauris nulla risus, pellentesque a porttitor efficitur, volutpat quis tellus. Duis eget scelerisque diam. Aliquam cursus mattis leo, et consequat magna porttitor vitae. Mauris tincidunt purus quis libero dignissim, ac gravida sem faucibus.
"""

lorem03 = """Phasellus luctus condimentum nunc, in dignissim purus placerat nec. Cras consequat sem ac lobortis vulputate. Sed condimentum commodo leo ut dignissim. Aliquam fermentum tortor fermentum turpis bibendum sodales nec sit amet nulla. Phasellus at neque vel nunc lobortis dictum. Maecenas sed laoreet enim. Vestibulum id interdum justo.
Cras fermentum lacus at accumsan pellentesque. Nam facilisis volutpat dignissim. Suspendisse turpis enim, fringilla id lacus ac, euismod finibus dui. Morbi ut neque a odio faucibus finibus. Suspendisse tincidunt elit neque, ut aliquet magna venenatis ut. Aliquam erat volutpat. Nullam ut arcu vel augue scelerisque maximus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec eleifend vulputate quam, vitae ultricies leo efficitur vitae. Etiam quis finibus dolor. Duis rhoncus enim a neque ornare egestas. Aliquam augue tellus, tempor at viverra at, vulputate eget nisi.
Etiam vitae hendrerit tellus. Duis dui diam, aliquet a vehicula quis, gravida ut lacus. Integer posuere dui vitae sollicitudin iaculis. Donec at nibh urna. Nunc et ultricies magna. Sed ullamcorper ac nisi sed aliquam. Curabitur tortor felis, tempor quis lectus placerat, hendrerit eleifend quam.
"""

lorem04 = """Integer at libero vel nunc dignissim sodales. Sed ipsum nunc, iaculis id maximus eget, luctus at lorem. Ut ullamcorper massa arcu, gravida facilisis erat varius eu. Morbi at placerat massa, sed semper sapien. Sed venenatis malesuada velit nec rutrum. Integer ullamcorper ligula augue, quis aliquet nisi sagittis sit amet. In a arcu vel diam eleifend congue pellentesque non massa. Etiam in ultrices arcu. Vivamus mollis ac lectus non blandit. Cras eros nulla, egestas a porta eget, faucibus et nulla. Morbi porttitor enim eget eros congue facilisis. In posuere dictum mi, vel dignissim risus congue quis. Integer quis arcu eu enim scelerisque porttitor. Sed vitae tempus metus. Duis vel enim tristique, tristique tellus vel, interdum sapien.
Phasellus quis odio volutpat felis euismod faucibus. Nunc quis arcu at urna cursus ultricies. In ex nisl, semper vitae molestie quis, varius et mauris. Etiam molestie faucibus lacus nec placerat. Donec pellentesque faucibus ex, ac pellentesque erat efficitur eleifend. Donec vehicula, sem sit amet cursus interdum, est lacus pretium elit, et dapibus nisl nunc non ipsum. Nunc mattis eros a fringilla tincidunt. In nisi arcu, lobortis elementum varius eu, malesuada eget diam. Praesent quis sodales libero. Nulla maximus turpis vitae malesuada sollicitudin. Vivamus id neque sagittis, interdum nunc eget, interdum purus.
Fusce a felis sit amet ex euismod euismod. Nulla facilisi. Vestibulum velit diam, convallis ac quam nec, dictum pharetra turpis. Nullam et rutrum felis. Aenean id iaculis tellus. Nulla facilisi. Pellentesque eu urna erat.
Maecenas posuere pretium nisl non semper. Duis auctor sem non aliquet mollis. Phasellus mattis ex sit amet dolor malesuada ornare. Etiam pharetra id dui vitae dignissim. Vivamus convallis odio nec ipsum faucibus consectetur. Nulla non gravida diam. Donec dapibus dolor quis est sagittis, tempor egestas mi mollis. Morbi ac nibh pretium, commodo lorem sit amet, dapibus odio. Phasellus porta ac sapien non eleifend. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse vulputate dui sed dui dignissim vestibulum.
"""

lorem05 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam consectetur magna tortor, pretium vestibulum metus efficitur sed. Morbi imperdiet mi ipsum, vel pharetra lacus aliquam sit amet. Quisque eget molestie metus. Duis ut diam mattis, vulputate leo iaculis, vulputate mi. Suspendisse fringilla interdum ante, nec porttitor elit convallis non. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porta imperdiet luctus. Integer congue sit amet odio mollis maximus. Vestibulum lacinia orci vitae consectetur auctor. Nullam risus felis, molestie sit amet ex at, bibendum lacinia risus. Phasellus pellentesque quam diam, ut imperdiet risus ultricies a. Curabitur convallis libero ac ante tincidunt consequat. Nulla facilisi. Nunc eleifend vitae diam eu maximus.
Aliquam et est in metus eleifend rutrum vel nec elit. Donec sit amet neque sollicitudin, egestas nulla in, rhoncus massa. Morbi fringilla ac nunc tincidunt dignissim. Mauris sapien orci, viverra vitae quam eget, cursus ornare ante. Nullam sed rutrum elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultricies sollicitudin molestie. Suspendisse laoreet placerat enim, vitae vestibulum lacus vulputate at. Vestibulum consectetur, erat at vehicula condimentum, ex nulla suscipit mauris, quis aliquet mi enim a ante. Suspendisse at mollis elit, non luctus lectus. Aliquam consequat diam eget lacus vulputate, et egestas tellus malesuada. Integer consequat sem ut velit finibus tempus. Vestibulum gravida varius vulputate. Fusce lacus velit, egestas sit amet mauris vel, posuere mollis massa.
Aenean eget pellentesque magna, eu elementum nunc. Phasellus quis ornare ante. Mauris volutpat, felis ac egestas luctus, tellus lectus tristique risus, ultrices semper quam nisi vitae turpis. Integer tincidunt nisi ut luctus rhoncus. Praesent sagittis vel lectus sed maximus. Maecenas vitae posuere felis. Curabitur venenatis magna a dignissim blandit. Nunc scelerisque lorem ipsum. Donec quis lacinia arcu. Phasellus sollicitudin, libero at semper imperdiet, nulla urna vulputate nisl, sit amet blandit sem dolor eu nibh. Cras diam arcu, lacinia id risus a, commodo lobortis ipsum. Sed elementum pulvinar tellus ut rhoncus. Vestibulum nec enim suscipit, condimentum magna sit amet, rutrum velit. Praesent non tortor eu diam hendrerit ultrices. Maecenas sit amet vestibulum tortor.
Nam vitae enim purus. Donec vulputate laoreet porta. Ut gravida, erat at tempor dictum, arcu nisi efficitur metus, dapibus gravida augue dui a nisl. Etiam elit diam, scelerisque eget tristique in, facilisis eget dolor. Integer auctor placerat elementum. Maecenas bibendum vitae ex at tempus. Sed porta dui non neque mollis, eleifend egestas sem accumsan. Nunc placerat leo vel elit pulvinar, quis vestibulum felis sagittis. Pellentesque eu orci dui. Nulla justo ipsum, lobortis efficitur lectus vitae, suscipit finibus est. Ut et nisi quis mauris pulvinar pretium et vitae tellus.
Aenean quam ex, tristique ut vehicula et, tempus vitae eros. Ut tempor sem purus, ut ultrices leo volutpat nec. Suspendisse dapibus tincidunt sollicitudin. Sed convallis, nisl ut mattis tincidunt, velit justo condimentum lectus, et tristique dolor purus in mi. Duis vitae dui a elit tempus rhoncus. Cras posuere, ligula et facilisis pellentesque, arcu felis tristique elit, et condimentum turpis magna vel tellus. Vivamus eget varius velit. Maecenas lacinia felis sit amet leo pellentesque, at dignissim dolor dictum. Etiam nibh augue, pretium id consectetur in, maximus finibus eros. Duis aliquet ante eget risus dictum hendrerit.
"""

articles = [
    {"text": lorem01, "paragraphs": 1, "words": 125},
    {"text": lorem02, "paragraphs": 2, "words": 217},
    {"text": lorem03, "paragraphs": 3, "words": 180},
    {"text": lorem04, "paragraphs": 4, "words": 323},
    {"text": lorem05, "paragraphs": 5, "words": 519},
]

def get_articles(n, user, paragraphs = 1):
    if paragraphs < 1 or paragraphs > len(articles):
        raise Exception(f"paragraphs must be in the range 1 to {len(articles)}, got {paragraphs}")

    unique_articles = []

    for i in range(n):
        seq = f"{i:03d}"
        ix = i % len(articles)
        # title must be unique, so we add "by {user} ({seq})" to it.
        article = {
            "title": f"{titles[ix]} by {user} ({seq})",
            "description": descriptions[ix],
            "body": articles[paragraphs - 1]["text"],
            "tagList": [tags[ix], tags[(ix + 1) % len(articles)]]
        }
        unique_articles.append(article)

    return unique_articles
