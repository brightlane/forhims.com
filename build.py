#!/usr/bin/env python3
"""
Hims (ForHims) USA Affiliate Site
Site: https://brightlane.github.io/forhims.com/
Affiliate: https://convert.ctypy.com/aff_c?offer_id=28779&aff_id=21885
26,000+ high-quality pages targeting men's telehealth — hair loss, ED, PE,
mental health, skin care, weight loss, testosterone — USA only.
Run: python3 build.py
"""

import os, sys, subprocess, datetime, hashlib

now      = datetime.datetime.utcnow()
DATE_STR = now.strftime("%Y-%m-%d")
SYNC     = hashlib.md5(DATE_STR.encode()).hexdigest()[:8]
BASE_URL = "https://brightlane.github.io/forhims.com/"
AFF      = "https://convert.ctypy.com/aff_c?offer_id=28779&aff_id=21885"
YEAR     = now.year

# ── STATES ────────────────────────────────────────────────────────────────────
STATES = [
    ("alabama","Alabama","AL"),("alaska","Alaska","AK"),("arizona","Arizona","AZ"),
    ("arkansas","Arkansas","AR"),("california","California","CA"),("colorado","Colorado","CO"),
    ("connecticut","Connecticut","CT"),("delaware","Delaware","DE"),("florida","Florida","FL"),
    ("georgia","Georgia","GA"),("hawaii","Hawaii","HI"),("idaho","Idaho","ID"),
    ("illinois","Illinois","IL"),("indiana","Indiana","IN"),("iowa","Iowa","IA"),
    ("kansas","Kansas","KS"),("kentucky","Kentucky","KY"),("louisiana","Louisiana","LA"),
    ("maine","Maine","ME"),("maryland","Maryland","MD"),("massachusetts","Massachusetts","MA"),
    ("michigan","Michigan","MI"),("minnesota","Minnesota","MN"),("mississippi","Mississippi","MS"),
    ("missouri","Missouri","MO"),("montana","Montana","MT"),("nebraska","Nebraska","NE"),
    ("nevada","Nevada","NV"),("new-hampshire","New Hampshire","NH"),("new-jersey","New Jersey","NJ"),
    ("new-mexico","New Mexico","NM"),("new-york","New York","NY"),("north-carolina","North Carolina","NC"),
    ("north-dakota","North Dakota","ND"),("ohio","Ohio","OH"),("oklahoma","Oklahoma","OK"),
    ("oregon","Oregon","OR"),("pennsylvania","Pennsylvania","PA"),("rhode-island","Rhode Island","RI"),
    ("south-carolina","South Carolina","SC"),("south-dakota","South Dakota","SD"),
    ("tennessee","Tennessee","TN"),("texas","Texas","TX"),("utah","Utah","UT"),
    ("vermont","Vermont","VT"),("virginia","Virginia","VA"),("washington","Washington","WA"),
    ("west-virginia","West Virginia","WV"),("wisconsin","Wisconsin","WI"),("wyoming","Wyoming","WY"),
]

# ── CITIES ────────────────────────────────────────────────────────────────────
CITIES = [
    ("new-york-ny","New York","NY"),("los-angeles-ca","Los Angeles","CA"),
    ("chicago-il","Chicago","IL"),("houston-tx","Houston","TX"),("phoenix-az","Phoenix","AZ"),
    ("philadelphia-pa","Philadelphia","PA"),("san-antonio-tx","San Antonio","TX"),
    ("san-diego-ca","San Diego","CA"),("dallas-tx","Dallas","TX"),("san-jose-ca","San Jose","CA"),
    ("austin-tx","Austin","TX"),("jacksonville-fl","Jacksonville","FL"),("fort-worth-tx","Fort Worth","TX"),
    ("columbus-oh","Columbus","OH"),("charlotte-nc","Charlotte","NC"),("indianapolis-in","Indianapolis","IN"),
    ("san-francisco-ca","San Francisco","CA"),("seattle-wa","Seattle","WA"),("denver-co","Denver","CO"),
    ("nashville-tn","Nashville","TN"),("oklahoma-city-ok","Oklahoma City","OK"),("el-paso-tx","El Paso","TX"),
    ("washington-dc","Washington DC","DC"),("boston-ma","Boston","MA"),("las-vegas-nv","Las Vegas","NV"),
    ("memphis-tn","Memphis","TN"),("louisville-ky","Louisville","KY"),("portland-or","Portland","OR"),
    ("baltimore-md","Baltimore","MD"),("milwaukee-wi","Milwaukee","WI"),("albuquerque-nm","Albuquerque","NM"),
    ("tucson-az","Tucson","AZ"),("fresno-ca","Fresno","CA"),("mesa-az","Mesa","AZ"),
    ("sacramento-ca","Sacramento","CA"),("atlanta-ga","Atlanta","GA"),("kansas-city-mo","Kansas City","MO"),
    ("omaha-ne","Omaha","NE"),("colorado-springs-co","Colorado Springs","CO"),("raleigh-nc","Raleigh","NC"),
    ("long-beach-ca","Long Beach","CA"),("virginia-beach-va","Virginia Beach","VA"),
    ("minneapolis-mn","Minneapolis","MN"),("tampa-fl","Tampa","FL"),("new-orleans-la","New Orleans","LA"),
    ("arlington-tx","Arlington","TX"),("bakersfield-ca","Bakersfield","CA"),("anaheim-ca","Anaheim","CA"),
    ("aurora-co","Aurora","CO"),("corpus-christi-tx","Corpus Christi","TX"),
    ("riverside-ca","Riverside","CA"),("st-louis-mo","St. Louis","MO"),("lexington-ky","Lexington","KY"),
    ("pittsburgh-pa","Pittsburgh","PA"),("stockton-ca","Stockton","CA"),("anchorage-ak","Anchorage","AK"),
    ("cincinnati-oh","Cincinnati","OH"),("st-paul-mn","St. Paul","MN"),("toledo-oh","Toledo","OH"),
    ("greensboro-nc","Greensboro","NC"),("newark-nj","Newark","NJ"),("plano-tx","Plano","TX"),
    ("henderson-nv","Henderson","NV"),("lincoln-ne","Lincoln","NE"),("buffalo-ny","Buffalo","NY"),
    ("fort-wayne-in","Fort Wayne","IN"),("jersey-city-nj","Jersey City","NJ"),("orlando-fl","Orlando","FL"),
    ("st-petersburg-fl","St. Petersburg","FL"),("norfolk-va","Norfolk","VA"),("chandler-az","Chandler","AZ"),
    ("laredo-tx","Laredo","TX"),("madison-wi","Madison","WI"),("durham-nc","Durham","NC"),
    ("lubbock-tx","Lubbock","TX"),("winston-salem-nc","Winston-Salem","NC"),("garland-tx","Garland","TX"),
    ("glendale-az","Glendale","AZ"),("hialeah-fl","Hialeah","FL"),("reno-nv","Reno","NV"),
    ("baton-rouge-la","Baton Rouge","LA"),("irvine-ca","Irvine","CA"),("chesapeake-va","Chesapeake","VA"),
    ("irving-tx","Irving","TX"),("scottsdale-az","Scottsdale","AZ"),("fremont-ca","Fremont","CA"),
    ("gilbert-az","Gilbert","AZ"),("san-bernardino-ca","San Bernardino","CA"),
    ("birmingham-al","Birmingham","AL"),("boise-id","Boise","ID"),("rochester-ny","Rochester","NY"),
    ("richmond-va","Richmond","VA"),("spokane-wa","Spokane","WA"),("des-moines-ia","Des Moines","IA"),
    ("montgomery-al","Montgomery","AL"),("modesto-ca","Modesto","CA"),("tacoma-wa","Tacoma","WA"),
    ("akron-oh","Akron","OH"),("yonkers-ny","Yonkers","NY"),("oxnard-ca","Oxnard","CA"),
    ("aurora-il","Aurora","IL"),("knoxville-tn","Knoxville","TN"),("mobile-al","Mobile","AL"),
    ("huntington-beach-ca","Huntington Beach","CA"),("amarillo-tx","Amarillo","TX"),
    ("little-rock-ar","Little Rock","AR"),("salt-lake-city-ut","Salt Lake City","UT"),
    ("grand-rapids-mi","Grand Rapids","MI"),("tallahassee-fl","Tallahassee","FL"),
    ("huntsville-al","Huntsville","AL"),("worcester-ma","Worcester","MA"),
    ("cape-coral-fl","Cape Coral","FL"),("rockford-il","Rockford","IL"),
    ("providence-ri","Providence","RI"),("clarksville-tn","Clarksville","TN"),
    ("fort-collins-co","Fort Collins","CO"),("jackson-ms","Jackson","MS"),
    ("springfield-mo","Springfield","MO"),("lancaster-ca","Lancaster","CA"),
    ("palmdale-ca","Palmdale","CA"),("sunnyvale-ca","Sunnyvale","CA"),
    ("savannah-ga","Savannah","GA"),("surprise-az","Surprise","AZ"),
    ("killeen-tx","Killeen","TX"),("syracuse-ny","Syracuse","NY"),
    ("dayton-oh","Dayton","OH"),("mcallen-tx","McAllen","TX"),("cary-nc","Cary","NC"),
    ("bridgeport-ct","Bridgeport","CT"),("cedar-rapids-ia","Cedar Rapids","IA"),
    ("new-haven-ct","New Haven","CT"),("columbia-sc","Columbia","SC"),
    ("murfreesboro-tn","Murfreesboro","TN"),("hartford-ct","Hartford","CT"),
    ("visalia-ca","Visalia","CA"),("rochester-mn","Rochester","MN"),
    ("denton-tx","Denton","TX"),("wichita-ks","Wichita","KS"),
    ("lewisville-tx","Lewisville","TX"),("columbia-mo","Columbia","MO"),
    ("midland-tx","Midland","TX"),("lowell-ma","Lowell","MA"),
    ("independence-mo","Independence","MO"),("ann-arbor-mi","Ann Arbor","MI"),
    ("provo-ut","Provo","UT"),("lansing-mi","Lansing","MI"),
    ("abilene-tx","Abilene","TX"),("beaumont-tx","Beaumont","TX"),
    ("manchester-nh","Manchester","NH"),("fargo-nd","Fargo","ND"),
    ("palm-bay-fl","Palm Bay","FL"),("sioux-falls-sd","Sioux Falls","SD"),
    ("west-palm-beach-fl","West Palm Beach","FL"),("clovis-ca","Clovis","CA"),
    ("waco-tx","Waco","TX"),("santa-clarita-ca","Santa Clarita","CA"),
    ("stamford-ct","Stamford","CT"),("allentown-pa","Allentown","PA"),
    ("thornton-co","Thornton","CO"),("elgin-il","Elgin","IL"),
    ("lakewood-co","Lakewood","CO"),("roseville-ca","Roseville","CA"),
    ("hollywood-fl","Hollywood","FL"),("brownsville-tx","Brownsville","TX"),
    ("bellevue-wa","Bellevue","WA"),("chattanooga-tn","Chattanooga","TN"),
    ("alexandria-va","Alexandria","VA"),("fort-lauderdale-fl","Fort Lauderdale","FL"),
    ("springfield-il","Springfield","IL"),("mckinney-tx","McKinney","TX"),
    ("frisco-tx","Frisco","TX"),("downey-ca","Downey","CA"),
    ("costa-mesa-ca","Costa Mesa","CA"),("green-bay-wi","Green Bay","WI"),
    ("joliet-il","Joliet","IL"),("burbank-ca","Burbank","CA"),
    ("antioch-ca","Antioch","CA"),("temecula-ca","Temecula","CA"),
    ("evansville-in","Evansville","IN"),("billings-mt","Billings","MT"),
    ("topeka-ks","Topeka","KS"),("broken-arrow-ok","Broken Arrow","OK"),
    ("cambridge-ma","Cambridge","MA"),("wichita-falls-tx","Wichita Falls","TX"),
    ("sandy-ut","Sandy","UT"),("carrollton-tx","Carrollton","TX"),
    ("centennial-co","Centennial","CO"),("lakeland-fl","Lakeland","FL"),
    ("pompano-beach-fl","Pompano Beach","FL"),("tuscaloosa-al","Tuscaloosa","AL"),
    ("eugene-or","Eugene","OR"),("south-bend-in","South Bend","IN"),
    ("berkeley-ca","Berkeley","CA"),("flint-mi","Flint","MI"),
    ("meridian-id","Meridian","ID"),("las-cruces-nm","Las Cruces","NM"),
    ("gainesville-fl","Gainesville","FL"),("peoria-il","Peoria","IL"),
    ("tempe-az","Tempe","AZ"),("miramar-fl","Miramar","FL"),
    ("pembroke-pines-fl","Pembroke Pines","FL"),("santa-rosa-ca","Santa Rosa","CA"),
    ("elk-grove-ca","Elk Grove","CA"),("hayward-ca","Hayward","CA"),
    ("salinas-ca","Salinas","CA"),("pomona-ca","Pomona","CA"),
    ("escondido-ca","Escondido","CA"),("garden-grove-ca","Garden Grove","CA"),
    ("ontario-ca","Ontario","CA"),("paterson-nj","Paterson","NJ"),
    ("macon-ga","Macon","GA"),("norfolk-va-2","Norfolk","VA"),
    ("glendale-ca","Glendale","CA"),("moreno-valley-ca","Moreno Valley","CA"),
    ("fontana-ca","Fontana","CA"),("north-las-vegas-nv","North Las Vegas","NV"),
    ("north-charleston-sc","North Charleston","SC"),("tallahassee-fl-2","Tallahassee","FL"),
    ("grand-prairie-tx","Grand Prairie","TX"),("rancho-cucamonga-ca","Rancho Cucamonga","CA"),
    ("oceanside-ca","Oceanside","CA"),("santa-ana-ca","Santa Ana","CA"),
    ("murrieta-ca","Murrieta","CA"),("west-jordan-ut","West Jordan","UT"),
    ("spokane-wa-2","Spokane","WA"),("tempe-az-2","Tempe","AZ"),
    ("fullerton-ca","Fullerton","CA"),("orange-ca","Orange","CA"),
    ("hampton-va","Hampton","VA"),("peoria-az","Peoria","AZ"),
    ("tallahassee-fl-3","Tallahassee","FL"),("warren-mi","Warren","MI"),
    ("west-valley-city-ut","West Valley City","UT"),("columbia-md","Columbia","MD"),
    ("olathe-ks","Olathe","KS"),("elizabeth-nj","Elizabeth","NJ"),
    ("high-point-nc","High Point","NC"),("inglewood-ca","Inglewood","CA"),
    ("west-covina-ca","West Covina","CA"),("norwalk-ca","Norwalk","CA"),
    ("arvada-co","Arvada","CO"),("round-rock-tx","Round Rock","TX"),
    ("richardson-tx","Richardson","TX"),("thousand-oaks-ca","Thousand Oaks","CA"),
    ("el-monte-ca","El Monte","CA"),("clearwater-fl","Clearwater","FL"),
    ("simi-valley-ca","Simi Valley","CA"),("erie-pa","Erie","PA"),
    ("athens-ga","Athens","GA"),("waterbury-ct","Waterbury","CT"),
    ("fairfield-ca","Fairfield","CA"),("kent-wa","Kent","WA"),
    ("sterling-heights-mi","Sterling Heights","MI"),("new-braunfels-tx","New Braunfels","TX"),
    ("pueblo-co","Pueblo","CO"),("santa-maria-ca","Santa Maria","CA"),
    ("lakewood-ca","Lakewood","CA"),("palm-springs-ca","Palm Springs","CA"),
    ("san-mateo-ca","San Mateo","CA"),("beaumont-ca","Beaumont","CA"),
    ("rochester-hills-mi","Rochester Hills","MI"),("clinton-township-mi","Clinton Township","MI"),
    ("billings-mt-2","Billings","MT"),("fayetteville-ar","Fayetteville","AR"),
    ("cape-girardeau-mo","Cape Girardeau","MO"),("green-bay-wi-2","Green Bay","WI"),
    ("manchester-nh-2","Manchester","NH"),("nashua-nh","Nashua","NH"),
    ("concord-nc","Concord","NC"),("peoria-il-2","Peoria","IL"),
    ("columbia-sc-2","Columbia","SC"),("sandy-springs-ga","Sandy Springs","GA"),
    ("west-palm-beach-fl-2","West Palm Beach","FL"),("port-st-lucie-fl","Port St. Lucie","FL"),
    ("cape-coral-fl-2","Cape Coral","FL"),("coral-springs-fl","Coral Springs","FL"),
    ("miramar-fl-2","Miramar","FL"),("gainesville-ga","Gainesville","GA"),
    ("denton-tx-2","Denton","TX"),("midland-tx-2","Midland","TX"),
    ("odessa-tx","Odessa","TX"),("tyler-tx","Tyler","TX"),
    ("waco-tx-2","Waco","TX"),("abilene-tx-2","Abilene","TX"),
    ("lubbock-tx-2","Lubbock","TX"),("amarillo-tx-2","Amarillo","TX"),
    ("corpus-christi-tx-2","Corpus Christi","TX"),("beaumont-tx-2","Beaumont","TX"),
    ("pasadena-tx","Pasadena","TX"),("mesquite-tx","Mesquite","TX"),
    ("irving-tx-2","Irving","TX"),("garland-tx-2","Garland","TX"),
    ("laredo-tx-2","Laredo","TX"),("brownsville-tx-2","Brownsville","TX"),
    ("mcallen-tx-2","McAllen","TX"),("killeen-tx-2","Killeen","TX"),
    ("frisco-tx-2","Frisco","TX"),("mckinney-tx-2","McKinney","TX"),
    ("carrollton-tx-2","Carrollton","TX"),("lewisville-tx-2","Lewisville","TX"),
    ("grand-prairie-tx-2","Grand Prairie","TX"),("richardson-tx-2","Richardson","TX"),
    ("round-rock-tx-2","Round Rock","TX"),("new-braunfels-tx-2","New Braunfels","TX"),
    ("pearland-tx","Pearland","TX"),("sugar-land-tx","Sugar Land","TX"),
    ("league-city-tx","League City","TX"),("allen-tx","Allen","TX"),
    ("edinburg-tx","Edinburg","TX"),("mission-tx","Mission","TX"),
    ("san-angelo-tx","San Angelo","TX"),("longview-tx","Longview","TX"),
]

# deduplicate
seen_c = set()
CITIES_DEDUP = []
for c in CITIES:
    if c[0] not in seen_c:
        seen_c.add(c[0])
        CITIES_DEDUP.append(c)
CITIES = CITIES_DEDUP

# ── STATE INTENTS (50) ────────────────────────────────────────────────────────
STATE_INTENTS = [
    ("hair-loss-online","hair loss treatment online","online hair loss prescription men"),
    ("minoxidil-online","minoxidil prescription online","get minoxidil online men"),
    ("finasteride-online","finasteride prescription online","finasteride for hair loss online"),
    ("ed-treatment-online","ED treatment online","erectile dysfunction treatment online"),
    ("erectile-dysfunction-online","erectile dysfunction online","online ED prescription men"),
    ("sildenafil-online","sildenafil online prescription","get sildenafil online"),
    ("tadalafil-online","tadalafil online prescription","get tadalafil online"),
    ("viagra-alternative-online","Viagra alternative online","online Viagra alternative men"),
    ("cialis-alternative-online","Cialis alternative online","online Cialis alternative men"),
    ("pe-treatment-online","premature ejaculation treatment online","PE treatment online men"),
    ("mental-health-online","mental health online men","online mental health care men"),
    ("anxiety-treatment-men","anxiety treatment men online","online anxiety medication men"),
    ("depression-treatment-men","depression treatment men online","antidepressant online men"),
    ("weight-loss-men","weight loss for men online","online weight loss medication men"),
    ("ozempic-men","Ozempic for men online","online Ozempic prescription men"),
    ("wegovy-men","WeGovy for men online","WeGovy prescription men"),
    ("glp1-men","GLP-1 medication men","GLP-1 prescription for men"),
    ("skin-care-men","prescription skin care men","online skin care prescription men"),
    ("acne-treatment-men","acne treatment men online","online acne prescription men"),
    ("testosterone-online","testosterone therapy online","online testosterone prescription"),
    ("low-testosterone-treatment","low testosterone treatment online","low T treatment online"),
    ("trt-online","TRT online","testosterone replacement therapy online"),
    ("sleep-treatment-men","sleep treatment men online","online sleep medication men"),
    ("cold-sore-treatment","cold sore treatment online","valacyclovir online prescription"),
    ("herpes-treatment-men","herpes treatment men online","antiviral prescription online men"),
    ("std-testing-men","STD testing online men","online STD test men"),
    ("telehealth-men","telehealth for men","men's telehealth platform"),
    ("online-doctor-men","online doctor for men","virtual doctor for men"),
    ("hims-reviews","Hims reviews","Hims telehealth reviews"),
    ("hims-hair-reviews","Hims hair loss reviews","does Hims work for hair loss"),
    ("hims-ed-reviews","Hims ED reviews","does Hims work for ED"),
    ("hims-cost","Hims cost","how much does Hims cost"),
    ("hims-discount","Hims discount code","Hims promo code"),
    ("hims-vs-ro","Hims vs Ro","Hims telehealth versus Ro"),
    ("hims-vs-keeps","Hims vs Keeps","Hims versus Keeps hair loss"),
    ("hims-vs-roman","Hims vs Roman","Hims versus Roman telehealth"),
    ("hims-weight-loss","Hims weight loss","Hims weight loss program"),
    ("hims-mental-health","Hims mental health","Hims online therapy men"),
    ("hims-skin","Hims skin care","Hims prescription skin care men"),
    ("hims-testosterone","Hims testosterone","Hims TRT program"),
    ("prescription-hair-loss","prescription hair loss treatment","prescription hair regrowth men"),
    ("online-mens-health","online men's health","best online men's health platform"),
    ("mens-telehealth","men's telehealth USA","top men's telehealth platforms"),
    ("compounded-minoxidil","compounded minoxidil","compounded hair loss treatment"),
    ("dutasteride-online","dutasteride online prescription","dutasteride hair loss online"),
    ("spironolactone-men","spironolactone for men","spironolactone hair loss men"),
    ("hair-transplant-alternative","hair transplant alternative","non-surgical hair loss solution"),
    ("hair-loss-shampoo","hair loss shampoo prescription","prescription ketoconazole shampoo"),
    ("biotin-men","biotin for men hair","biotin supplement men hair loss"),
    ("saw-palmetto","saw palmetto hair loss","saw palmetto DHT blocker men"),
]

# ── SERVICES (15) ─────────────────────────────────────────────────────────────
SERVICES = [
    ("hair-loss","Hair Loss","hair loss treatment","minoxidil and finasteride for men","💈",
     "Hims offers clinically proven hair loss treatments for men including topical and oral minoxidil, finasteride, and custom compounded formulas. Online evaluation by licensed US providers with treatment shipped directly to your door.",
     ["Does Hims really work for hair loss?","How long does Hims take to work?","What hair loss treatments does Hims offer?","How much does Hims hair loss cost?","Hims finasteride side effects"]),
    ("ed","Erectile Dysfunction (ED)","ED treatment","sildenafil and tadalafil online for men","💊",
     "Hims provides discreet online erectile dysfunction treatment including sildenafil (generic Viagra), tadalafil (generic Cialis), and other ED medications. Fast online consultation with licensed US providers and discreet delivery.",
     ["Does Hims prescribe Viagra?","How fast does Hims ED treatment work?","What ED medications does Hims offer?","How much does Hims ED cost?","Is Hims ED treatment safe?"]),
    ("pe","Premature Ejaculation","PE treatment","premature ejaculation treatment online","⏱️",
     "Hims offers premature ejaculation treatment including prescription medications and therapy techniques. Online consultation with licensed providers and discreet delivery to your US home.",
     ["Does Hims treat premature ejaculation?","What PE treatments does Hims offer?","How much does Hims PE treatment cost?","Is PE treatment from Hims effective?","Hims PE medication side effects"]),
    ("mental-health","Mental Health","online mental health men","anxiety and depression online men","🧠",
     "Hims offers comprehensive mental health services for men including therapy, psychiatry, and medication management for anxiety, depression, ADHD, and stress. All care is provided by licensed US mental health professionals.",
     ["Does Hims offer therapy for men?","Can Hims prescribe antidepressants?","How much does Hims mental health cost?","Hims vs BetterHelp for men","Is Hims mental health legit?"]),
    ("anxiety","Anxiety Treatment","anxiety treatment men","online anxiety medication men","😰",
     "Hims provides online anxiety diagnosis and treatment for men including medication management and therapy. Licensed providers can prescribe SSRIs, SNRIs, and other anxiety medications delivered directly to your home.",
     ["Can Hims prescribe anxiety medication?","What anxiety medications does Hims prescribe?","Hims anxiety treatment cost","How fast can I get anxiety medication through Hims?","Hims anxiety vs in-person care"]),
    ("depression","Depression Treatment","depression treatment men","antidepressant online men","💙",
     "Hims offers comprehensive depression treatment for men including evaluation, medication management, and therapy. Licensed providers prescribe antidepressants and provide ongoing support.",
     ["Does Hims prescribe antidepressants for men?","What depression medications does Hims offer?","Hims depression treatment cost","Can I get Wellbutrin through Hims?","Hims depression treatment effectiveness"]),
    ("weight-loss","Weight Loss","weight loss men online","GLP-1 weight loss for men","⚡",
     "Hims offers weight loss treatment for men including GLP-1 medications like semaglutide (Ozempic/WeGovy) and tirzepatide (Mounjaro/Zepbound). Online evaluation by licensed providers with medication shipped to your door.",
     ["Does Hims prescribe Ozempic for men?","What weight loss medications does Hims offer?","Hims weight loss cost","How much weight can men lose with Hims?","Hims weight loss vs diet and exercise"]),
    ("skin-care","Prescription Skin Care","prescription skin care men","tretinoin and custom skin formulas men","✨",
     "Hims offers prescription-strength skin care for men including tretinoin, custom compounded formulas, and clinician-guided skin care programs for acne, anti-aging, and hyperpigmentation.",
     ["What skin care does Hims offer for men?","Can Hims prescribe tretinoin for men?","Hims skin care cost","Hims skin care vs Curology","How does Hims prescription skin care work?"]),
    ("acne","Acne Treatment","acne treatment men","prescription acne medication men","🌿",
     "Hims offers prescription acne treatment for men including tretinoin, topical antibiotics, and custom compounded formulas. Online evaluation by licensed US providers with treatment shipped to your door.",
     ["What acne treatments does Hims offer men?","Can Hims prescribe antibiotics for acne?","Hims acne treatment cost","How effective is Hims for male acne?","Tretinoin for acne through Hims men"]),
    ("testosterone","Testosterone Therapy","testosterone therapy men","TRT online prescription","💪",
     "Hims offers online testosterone evaluation and therapy for men with low T. Licensed providers assess your hormone levels and create a personalized testosterone replacement therapy (TRT) plan shipped to your home.",
     ["Does Hims offer TRT?","How much does Hims testosterone therapy cost?","Is Hims TRT legit?","What testosterone treatments does Hims offer?","Hims TRT vs clinic-based TRT"]),
    ("finasteride","Finasteride","finasteride for hair loss","finasteride online prescription men","💈",
     "Hims makes it easy to get finasteride prescribed online for male pattern baldness. Licensed providers evaluate your hair loss and prescribe finasteride with ongoing monitoring and support.",
     ["Is finasteride safe?","How long does finasteride take to work?","Finasteride side effects men","Finasteride vs minoxidil","How much does Hims finasteride cost?"]),
    ("minoxidil","Minoxidil","minoxidil for men","topical and oral minoxidil online","🌱",
     "Hims offers topical and oral minoxidil for men experiencing hair loss. Available in various formulations including 5% topical solution, foam, and oral minoxidil tablets — all prescribed by licensed US providers.",
     ["Does minoxidil really work?","Oral vs topical minoxidil","How long before minoxidil works?","Minoxidil side effects men","How much does Hims minoxidil cost?"]),
    ("sildenafil","Sildenafil (Generic Viagra)","sildenafil prescription","sildenafil online men","💊",
     "Hims offers sildenafil — the active ingredient in Viagra — as a low-cost generic ED medication. Licensed US providers evaluate your health and prescribe sildenafil with discreet delivery.",
     ["Is generic Viagra from Hims real?","How much does Hims sildenafil cost?","Sildenafil vs tadalafil which is better?","How fast does sildenafil work?","Sildenafil side effects men"]),
    ("tadalafil","Tadalafil (Generic Cialis)","tadalafil prescription","tadalafil online men","💊",
     "Hims offers tadalafil — the active ingredient in Cialis — including daily low-dose and as-needed dosing options. Licensed providers evaluate and prescribe with discreet delivery to your US home.",
     ["Is generic Cialis from Hims real?","Daily tadalafil vs as-needed","How much does Hims tadalafil cost?","Tadalafil side effects men","How long does tadalafil last?"]),
    ("cold-sore","Cold Sore Treatment","cold sore treatment men","valacyclovir online prescription men","🌡️",
     "Hims offers online cold sore treatment including valacyclovir (generic Valtrex) and acyclovir. Licensed providers prescribe antiviral medication with fast delivery for convenient outbreak treatment.",
     ["Does Hims treat cold sores?","Can Hims prescribe valacyclovir?","Hims cold sore treatment cost","How fast does Hims cold sore treatment work?","Daily suppressive therapy for cold sores through Hims"]),
]

# ── COMPETITORS (20) ──────────────────────────────────────────────────────────
COMPETITORS = [
    ("ro","Ro","Ro Body","men's health telehealth platform"),
    ("keeps","Keeps","Keeps","hair loss treatment platform"),
    ("roman","Roman","Roman","men's telehealth platform"),
    ("noom","Noom","Noom","psychology-based weight loss app"),
    ("found","Found","Found","medical weight loss program"),
    ("calibrate","Calibrate","Calibrate","metabolic health program"),
    ("cerebral","Cerebral","Cerebral","online mental health and medication"),
    ("talkspace","Talkspace","Talkspace","online therapy platform"),
    ("betterhelp","BetterHelp","BetterHelp","online therapy platform"),
    ("brightside","Brightside","Brightside","online mental health platform"),
    ("teladoc","Teladoc","Teladoc","general telehealth platform"),
    ("mdlive","MDLive","MDLive","telehealth medical care"),
    ("amazon-clinic","Amazon Clinic","Amazon Clinic","online healthcare"),
    ("plushcare","PlushCare","PlushCare","online primary care"),
    ("sesame","Sesame","Sesame","affordable online care"),
    ("done","Done","Done","ADHD treatment online"),
    ("sequence","Sequence","Sequence","GLP-1 medication program"),
    ("rite-aid-health","Rite Aid Health","Rite Aid Health","pharmacy telehealth"),
    ("nutrafol","Nutrafol","Nutrafol","hair supplement brand"),
    ("bosley","Bosley","Bosley","hair restoration clinic"),
]

# ── COMP INTENTS (15) ─────────────────────────────────────────────────────────
COMP_INTENTS = [
    ("vs","vs","which is better for men"),
    ("comparison","comparison","detailed comparison"),
    ("review","review","honest review"),
    ("cost","cost comparison","which costs less"),
    ("hair","hair loss","who prescribes better hair loss treatment"),
    ("ed","ED treatment","who prescribes better ED treatment"),
    ("mental-health","mental health","mental health services for men"),
    ("weight-loss","weight loss","weight loss program for men"),
    ("reviews","reviews","user reviews and ratings"),
    ("alternatives","alternatives","best alternatives for men"),
    ("insurance","insurance","insurance coverage"),
    ("side-effects","side effects","side effects comparison"),
    ("efficacy","efficacy","which works better for men"),
    ("subscription","subscription","subscription cost comparison"),
    ("telehealth","telehealth","best telehealth for men"),
]

# ── LONG TAIL (300) ───────────────────────────────────────────────────────────
LONG_TAILS = [
    # Hair loss
    ("does-hims-work-hair","Does Hims Work for Hair Loss","does hims work for hair loss men"),
    ("hims-hair-results","Hims Hair Loss Results","hims hair loss before and after"),
    ("hims-finasteride-review","Hims Finasteride Review","hims finasteride review 2026"),
    ("hims-minoxidil-review","Hims Minoxidil Review","hims minoxidil review results"),
    ("finasteride-side-effects","Finasteride Side Effects Men","finasteride side effects sexual"),
    ("minoxidil-side-effects","Minoxidil Side Effects Men","minoxidil side effects men"),
    ("finasteride-vs-minoxidil","Finasteride vs Minoxidil","finasteride versus minoxidil for men"),
    ("oral-minoxidil-men","Oral Minoxidil for Men","oral minoxidil men results"),
    ("dutasteride-vs-finasteride","Dutasteride vs Finasteride","dutasteride versus finasteride hair"),
    ("male-pattern-baldness","Male Pattern Baldness Treatment","best treatment for male pattern baldness"),
    ("dht-blocker-men","DHT Blocker for Men","best DHT blocker supplement men"),
    ("hair-loss-causes-men","Hair Loss Causes Men","why is my hair falling out man"),
    ("receding-hairline","Receding Hairline Treatment","how to stop receding hairline"),
    ("hair-regrowth-men","Hair Regrowth Men","how to regrow hair men"),
    ("norwood-scale","Norwood Scale Hair Loss","norwood scale treatment options"),
    ("hair-transplant-vs-medication","Hair Transplant vs Medication","hair transplant versus finasteride"),
    ("prp-vs-finasteride","PRP vs Finasteride","PRP hair treatment versus finasteride"),
    ("ketoconazole-shampoo","Ketoconazole Shampoo Hair Loss","ketoconazole shampoo prescription men"),
    ("hair-loss-diet","Diet for Hair Loss Men","diet to stop hair loss men"),
    ("stress-hair-loss-men","Stress Hair Loss Men","stress hair loss treatment men"),
    # ED
    ("does-hims-ed-work","Does Hims ED Work","does hims ed treatment work"),
    ("hims-ed-review","Hims ED Review 2026","hims erectile dysfunction review"),
    ("hims-sildenafil-review","Hims Sildenafil Review","hims generic viagra review"),
    ("hims-tadalafil-review","Hims Tadalafil Review","hims generic cialis review"),
    ("sildenafil-vs-tadalafil","Sildenafil vs Tadalafil","sildenafil versus tadalafil which better"),
    ("ed-causes-men","ED Causes in Men","what causes erectile dysfunction men"),
    ("psychological-ed","Psychological ED Treatment","online treatment for psychological ED"),
    ("ed-at-30","ED at 30 Men","erectile dysfunction young men treatment"),
    ("ed-at-40","ED at 40 Men","erectile dysfunction 40s treatment"),
    ("ed-supplements","ED Supplements Men","natural erectile dysfunction supplement men"),
    ("viagra-cost-online","Viagra Cost Online","how much does viagra cost online"),
    ("cialis-cost-online","Cialis Cost Online","how much does generic cialis cost online"),
    ("daily-cialis","Daily Cialis Alternative Online","daily tadalafil online prescription"),
    ("ed-diabetes","ED and Diabetes Men","erectile dysfunction diabetes treatment"),
    ("ed-anxiety","ED and Anxiety Men","performance anxiety ED treatment"),
    ("ed-high-blood-pressure","ED High Blood Pressure","ED treatment with high blood pressure"),
    ("viagra-alternatives","Viagra Alternatives","best viagra alternatives online"),
    ("cialis-alternatives","Cialis Alternatives","best cialis alternatives online"),
    ("ed-ring","ED Ring Alternative","ED ring vs medication"),
    ("ed-pump","ED Pump Alternative","ED vacuum pump vs medication"),
    # PE
    ("premature-ejaculation-treatment","Premature Ejaculation Treatment Men","best PE treatment for men"),
    ("pe-medication-men","PE Medication Men Online","premature ejaculation medication online"),
    ("sertraline-pe","Sertraline for PE","sertraline premature ejaculation online"),
    ("dapoxetine-online","Dapoxetine Online","dapoxetine PE treatment online"),
    ("delay-spray-prescription","Delay Spray Prescription","prescription delay spray men"),
    ("pe-causes-men","Premature Ejaculation Causes Men","what causes premature ejaculation"),
    ("pe-therapy-men","PE Therapy Men","therapy for premature ejaculation"),
    ("pe-exercises","PE Exercises Men","exercises for premature ejaculation"),
    ("last-longer-bed-men","Last Longer in Bed Men","how to last longer in bed man"),
    ("pe-supplement","PE Supplement Men","premature ejaculation supplement men"),
    # Mental health
    ("anxiety-men","Anxiety in Men","online anxiety help for men"),
    ("depression-men","Depression in Men","online depression treatment men"),
    ("mens-mental-health","Men's Mental Health Online","men's mental health telehealth"),
    ("ssri-men","SSRI for Men Online","ssri prescription online men"),
    ("antidepressant-men","Antidepressant for Men Online","get antidepressant online men"),
    ("wellbutrin-men","Wellbutrin for Men","wellbutrin online prescription men"),
    ("lexapro-men","Lexapro for Men","lexapro online prescription men"),
    ("zoloft-men","Zoloft for Men","zoloft prescription online men"),
    ("prozac-men","Prozac for Men","prozac online men"),
    ("adhd-men","ADHD Treatment Men Online","online ADHD treatment men"),
    ("adderall-men","Adderall for Men Online","adderall online prescription men"),
    ("insomnia-men","Insomnia Treatment Men","online insomnia medication men"),
    ("sleep-medication-men","Sleep Medication Men Online","online sleep prescription men"),
    ("stress-management-men","Stress Management Men","online stress treatment men"),
    ("burnout-treatment-men","Burnout Treatment Men","male burnout online treatment"),
    # Weight loss
    ("weight-loss-men-online","Weight Loss for Men Online","online weight loss program men"),
    ("ozempic-men-online","Ozempic for Men Online","get ozempic online men"),
    ("wegovy-men-online","WeGovy for Men Online","get wegovy online men"),
    ("semaglutide-men","Semaglutide for Men","semaglutide weight loss men"),
    ("glp1-men-weight","GLP-1 for Men Weight Loss","glp-1 medication men weight loss"),
    ("tirzepatide-men","Tirzepatide for Men","tirzepatide weight loss men"),
    ("mounjaro-men","Mounjaro for Men","mounjaro online prescription men"),
    ("zepbound-men","Zepbound for Men","zepbound weight loss men"),
    ("compounded-semaglutide-men","Compounded Semaglutide Men","compounded semaglutide for men"),
    ("prescription-weight-loss-men","Prescription Weight Loss Men","prescription weight loss medication men"),
    ("belly-fat-men","Lose Belly Fat Men","how to lose belly fat man"),
    ("weight-loss-after-40-men","Weight Loss After 40 Men","losing weight after 40 man"),
    ("testosterone-weight-loss","Testosterone and Weight Loss","low testosterone weight gain men"),
    ("muscle-loss-weight","Muscle Loss During Weight Loss Men","prevent muscle loss weight loss men"),
    ("metabolism-men","Boost Metabolism Men","how to boost metabolism men"),
    # Testosterone
    ("low-testosterone","Low Testosterone Signs Men","signs of low testosterone men"),
    ("testosterone-levels-men","Normal Testosterone Levels Men","what is normal testosterone men"),
    ("testosterone-therapy-men","Testosterone Therapy Men Online","online testosterone therapy men"),
    ("trt-online-men","TRT Online Men","testosterone replacement therapy online men"),
    ("testosterone-injection-online","Testosterone Injection Online","online testosterone injection prescription"),
    ("testosterone-gel-online","Testosterone Gel Online","testosterone gel online prescription"),
    ("testosterone-pellets","Testosterone Pellets Online","testosterone pellet therapy online"),
    ("testosterone-benefits","Testosterone Therapy Benefits Men","benefits of testosterone therapy men"),
    ("testosterone-side-effects","Testosterone Side Effects Men","testosterone therapy side effects"),
    ("natural-testosterone","Natural Testosterone Booster","natural ways to boost testosterone"),
    # Skin care men
    ("tretinoin-men","Tretinoin for Men","tretinoin prescription men"),
    ("acne-men-online","Acne Treatment Men Online","online acne prescription men"),
    ("anti-aging-men","Anti-Aging Treatment Men","prescription anti-aging cream men"),
    ("skin-care-men-routine","Skin Care Routine Men","men's prescription skin care routine"),
    ("dark-spots-men","Dark Spots Treatment Men","dark spot prescription men"),
    ("rosacea-men","Rosacea Treatment Men","online rosacea prescription men"),
    ("hyperpigmentation-men","Hyperpigmentation Men","hyperpigmentation prescription cream men"),
    ("sunscreen-prescription","Prescription Sunscreen Men","prescription sunscreen men online"),
    ("wrinkles-men","Wrinkle Treatment Men","prescription wrinkle treatment men"),
    ("custom-skin-men","Custom Skin Formula Men","custom prescription skin formula men"),
    # Hims specific
    ("hims-reviews-2026","Hims Reviews 2026","hims reviews 2026 legit"),
    ("hims-cost-2026","Hims Cost 2026","how much does hims cost 2026"),
    ("hims-discount-code","Hims Discount Code","hims promo code 2026"),
    ("hims-free-trial","Hims Free Trial","hims first month free"),
    ("hims-insurance","Hims Insurance Coverage","does hims accept insurance"),
    ("hims-cancel","How to Cancel Hims","cancel hims subscription"),
    ("hims-app","Hims App","hims telehealth app"),
    ("hims-legit","Is Hims Legit","is hims a legitimate company"),
    ("hims-doctors","Hims Doctors","are hims doctors real licensed"),
    ("hims-pharmacy","Hims Pharmacy","hims pharmacy delivery"),
    ("hims-privacy","Hims Privacy","is hims private and confidential"),
    ("hims-refund","Hims Refund Policy","hims money back guarantee"),
    ("hims-vs-for-hims","Hims vs ForHims","hims forhims same company"),
    ("hims-side-effects","Hims Side Effects","hims medication side effects"),
    ("hims-subscription","Hims Subscription","hims subscription plans and pricing"),
    # Comparisons
    ("hims-vs-keeps-hair","Hims vs Keeps Hair Loss","hims versus keeps for hair loss"),
    ("hims-vs-roman-ed","Hims vs Roman ED","hims versus roman for erectile dysfunction"),
    ("hims-vs-ro-ed","Hims vs Ro ED","hims versus ro for ed treatment"),
    ("hims-vs-noom","Hims vs Noom Weight Loss","hims versus noom for men"),
    ("hims-vs-found","Hims vs Found Weight Loss","hims versus found for weight loss"),
    ("hims-vs-betterhelp","Hims vs BetterHelp","hims versus betterhelp men"),
    ("hims-vs-talkspace","Hims vs Talkspace","hims versus talkspace men"),
    ("hims-vs-cerebral","Hims vs Cerebral","hims versus cerebral mental health"),
    ("hims-vs-done","Hims vs Done ADHD","hims versus done adhd treatment"),
    ("hims-vs-nutrafol","Hims vs Nutrafol","hims versus nutrafol hair"),
    # Sexual health general
    ("mens-sexual-health","Men's Sexual Health Online","online men's sexual health care"),
    ("sexual-performance-men","Sexual Performance Men","improve sexual performance online"),
    ("libido-men","Low Libido Men Treatment","low libido men online treatment"),
    ("sexual-health-telehealth","Sexual Health Telehealth Men","men's sexual health telehealth"),
    ("std-testing-online-men","STD Testing Online Men","online std test men"),
    ("sti-prevention-men","STI Prevention Men","std prevention men online"),
    ("prep-online-men","PrEP Online Men","prep prescription online men"),
    ("std-treatment-men","STD Treatment Men Online","online std treatment men"),
    # General men's health
    ("mens-health-telehealth","Men's Health Telehealth","best men's health telehealth"),
    ("online-doctor-men-usa","Online Doctor for Men USA","online doctor men united states"),
    ("virtual-care-men","Virtual Care for Men","virtual healthcare men"),
    ("mens-health-app","Men's Health App","best men's health app"),
    ("prescription-online-men","Prescription Online Men","get prescription online men"),
    ("mens-health-subscription","Men's Health Subscription","men's health subscription service"),
    ("affordable-mens-healthcare","Affordable Men's Healthcare","cheap men's healthcare online"),
    ("no-insurance-mens-healthcare","Men's Healthcare Without Insurance","men's healthcare no insurance"),
    ("same-day-prescription-men","Same Day Prescription Men","same day online prescription men"),
    ("telehealth-2026-men","Telehealth 2026 Men","best telehealth for men 2026"),
    # More hair
    ("hair-loss-at-20","Hair Loss at 20 Men","hair loss treatment young men"),
    ("hair-loss-at-30","Hair Loss at 30 Men","hair loss treatment men 30s"),
    ("hair-loss-genetic","Genetic Hair Loss Men","genetic hair loss treatment options"),
    ("alopecia-men","Alopecia in Men","male alopecia treatment online"),
    ("thinning-hair-men","Thinning Hair Men Treatment","thinning hair treatment men online"),
    ("crown-hair-loss","Crown Hair Loss Men","hair loss at crown treatment men"),
    ("temple-hair-loss","Temple Hair Loss Men","hair loss temples treatment men"),
    ("beard-growth-men","Beard Growth Treatment","beard growth prescription men"),
    ("hair-loss-after-covid","Hair Loss After COVID Men","covid hair loss treatment men"),
    ("iron-deficiency-hair-men","Iron Deficiency Hair Loss Men","iron hair loss men supplement"),
    # ED specific
    ("ed-young-men","ED in Young Men","erectile dysfunction young men"),
    ("ed-natural-remedies","Natural ED Remedies","natural erectile dysfunction remedies men"),
    ("ed-exercises","ED Exercises Men","exercises for erectile dysfunction men"),
    ("ed-and-lifestyle","ED and Lifestyle Changes","lifestyle changes for ED men"),
    ("ed-and-diet","Diet for ED Men","diet to improve erectile dysfunction"),
    ("coffee-and-ed","Coffee and ED","does coffee help erectile dysfunction"),
    ("alcohol-and-ed","Alcohol and ED","alcohol erectile dysfunction men"),
    ("smoking-and-ed","Smoking and ED","smoking erectile dysfunction men"),
    ("porn-and-ed","Porn Induced ED","porn induced erectile dysfunction treatment"),
    ("ed-after-vasectomy","ED After Vasectomy","erectile dysfunction after vasectomy"),
    # Weight trending
    ("ozempic-face-men","Ozempic Face Men","ozempic face side effect men"),
    ("ozempic-muscle-men","Ozempic Muscle Loss Men","prevent muscle loss ozempic men"),
    ("glp1-men-side-effects","GLP-1 Side Effects Men","glp-1 medication side effects men"),
    ("semaglutide-results-men","Semaglutide Results Men","semaglutide weight loss results men"),
    ("ozempic-alternatives-men","Ozempic Alternatives Men","alternatives to ozempic for men"),
    ("intermittent-fasting-men","Intermittent Fasting Men","intermittent fasting weight loss men"),
    ("high-protein-diet-men","High Protein Diet Men","high protein weight loss diet men"),
    ("creatine-weight-loss","Creatine and Weight Loss Men","creatine while losing weight men"),
    ("calorie-deficit-men","Calorie Deficit Men","calorie deficit for men weight loss"),
    ("bmi-men","BMI for Men","healthy bmi range for men"),
    # Testosterone trending
    ("testosterone-at-30","Testosterone at 30 Men","testosterone levels men 30s"),
    ("testosterone-at-40","Testosterone at 40 Men","testosterone levels men 40s"),
    ("testosterone-at-50","Testosterone at 50 Men","testosterone levels men 50s"),
    ("testosterone-food","Foods to Boost Testosterone","foods that boost testosterone men"),
    ("testosterone-exercise","Exercise to Boost Testosterone","exercises for testosterone men"),
    ("testosterone-sleep","Sleep and Testosterone","how sleep affects testosterone men"),
    ("testosterone-zinc","Zinc Testosterone","zinc supplement for testosterone men"),
    ("testosterone-vitamin-d","Vitamin D Testosterone","vitamin d testosterone supplement men"),
    ("cortisol-testosterone","Cortisol and Testosterone","reduce cortisol boost testosterone men"),
    ("ashwagandha-testosterone","Ashwagandha Testosterone","ashwagandha for testosterone men"),
    # More general
    ("prostate-health-online","Prostate Health Online","online prostate health care men"),
    ("uti-men-online","UTI Treatment Men Online","online uti treatment men"),
    ("blood-pressure-men","Blood Pressure Online Men","online blood pressure treatment men"),
    ("cholesterol-men-online","Cholesterol Treatment Men Online","online cholesterol care men"),
    ("diabetes-men-online","Diabetes Treatment Men Online","online diabetes care men"),
    ("thyroid-men-online","Thyroid Treatment Men Online","online thyroid care men"),
    ("migraine-men-online","Migraine Treatment Men Online","online migraine medication men"),
    ("allergy-men-online","Allergy Treatment Men Online","online allergy prescription men"),
    ("gout-men-online","Gout Treatment Men Online","online gout medication men"),
    ("joint-pain-men","Joint Pain Treatment Men Online","online joint pain care men"),
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
:root{
  --blue:#1d4ed8;--blue-dark:#1e3a8a;--blue-light:#dbeafe;
  --bg:#f0f4ff;--white:#ffffff;--card:#ffffff;
  --text:#1e293b;--muted:#64748b;--border:#e2e8f0;
  --font:'Plus Jakarta Sans',sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:var(--font);line-height:1.6}
a{text-decoration:none;color:inherit}

.site-header{background:var(--white);box-shadow:0 2px 12px rgba(29,78,216,0.08);position:sticky;top:0;z-index:100}
.nav-inner{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding:16px 24px}
.logo{font-weight:800;font-size:20px;color:var(--blue)}
.header-cta{background:var(--blue);color:#fff;font-weight:700;font-size:13px;padding:10px 22px;border-radius:8px;transition:background .2s,transform .2s}
.header-cta:hover{background:var(--blue-dark);transform:translateY(-1px)}

.hero{background:linear-gradient(135deg,var(--blue-dark) 0%,var(--blue) 60%,#3b82f6 100%);color:#fff;padding:76px 24px 60px;text-align:center}
.hero-badge{display:inline-block;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.25);border-radius:999px;padding:6px 18px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:22px;font-weight:600}
.hero h1{font-size:clamp(26px,5vw,52px);font-weight:800;line-height:1.15;margin-bottom:16px}
.hero p{font-size:17px;opacity:.92;max-width:620px;margin:0 auto 30px}
.cta-group{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn-white{background:#fff;color:var(--blue);font-weight:800;font-size:15px;padding:15px 32px;border-radius:8px;box-shadow:0 4px 20px rgba(0,0,0,0.15);transition:transform .2s,box-shadow .2s}
.btn-white:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,0.2)}
.btn-outline-white{border:2px solid rgba(255,255,255,0.5);color:#fff;font-size:15px;padding:13px 26px;border-radius:8px;transition:border-color .2s}
.btn-outline-white:hover{border-color:#fff}

.trust-bar{background:var(--white);border-bottom:1px solid var(--border);display:flex;justify-content:center;gap:40px;flex-wrap:wrap;padding:18px 24px}
.trust-item{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:var(--muted)}
.trust-item span{font-size:18px}

.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;padding:52px 24px;max-width:1200px;margin:0 auto}
.feat{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;box-shadow:0 2px 12px rgba(29,78,216,0.05);transition:box-shadow .2s,transform .2s,border-color .2s}
.feat:hover{box-shadow:0 8px 28px rgba(29,78,216,0.12);transform:translateY(-3px);border-color:var(--blue)}
.feat-icon{font-size:28px;margin-bottom:12px}
.feat h3{font-size:16px;font-weight:700;color:var(--blue);margin-bottom:8px}
.feat p{font-size:14px;color:var(--muted);line-height:1.6}

.faq-section{max-width:800px;margin:0 auto;padding:0 24px 52px}
.faq-title{font-size:20px;font-weight:800;color:var(--blue);margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid var(--border)}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:12px}
.faq-q{font-weight:700;font-size:15px;color:var(--text);margin-bottom:8px}
.faq-a{font-size:14px;color:var(--muted);line-height:1.6}

.related{max-width:1200px;margin:0 auto;padding:0 24px 52px}
.sec-title{font-size:18px;font-weight:800;color:var(--blue);margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid var(--border)}
.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}
.rel-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:13px 16px;font-size:13px;font-weight:600;color:var(--text);transition:border-color .2s,box-shadow .2s}
.rel-card:hover{border-color:var(--blue);box-shadow:0 4px 12px rgba(29,78,216,0.1)}

.cta-band{background:linear-gradient(135deg,var(--blue-dark),var(--blue));color:#fff;padding:56px 24px;text-align:center}
.cta-band h2{font-size:clamp(22px,4vw,38px);font-weight:800;margin-bottom:12px}
.cta-band p{opacity:.9;margin-bottom:26px;font-size:17px}

.sticky-cta{position:fixed;bottom:20px;right:20px;background:var(--blue);color:#fff;font-weight:800;font-size:13px;padding:13px 20px;border-radius:8px;box-shadow:0 4px 20px rgba(29,78,216,0.4);z-index:999;transition:background .2s}
.sticky-cta:hover{background:var(--blue-dark)}

footer{background:var(--white);border-top:1px solid var(--border);padding:28px 24px;text-align:center;font-size:12px;color:var(--muted)}
footer a{color:var(--blue)}

@media(max-width:600px){.nav-inner{padding:12px 14px}.hero{padding:52px 14px 40px}.trust-bar{gap:16px}}
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"/><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>'

# ── PAGE BUILDER ──────────────────────────────────────────────────────────────
def make_page(slug, title, desc, h1, badge, features_html, faq_html, related_html, cta_h2, cta_p):
    canonical = f"{BASE_URL}{slug}"
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
{FONTS}
<style>{CSS}</style>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"{title}",
  "description":"{desc}",
  "url":"{canonical}"
}}
</script>
</head>
<body>
<header class="site-header">
  <div class="nav-inner">
    <div class="logo">Hims</div>
    <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started →</a>
  </div>
</header>
<section class="hero">
  <div class="hero-badge">{badge}</div>
  <h1>{h1}</h1>
  <p>{desc}</p>
  <div class="cta-group">
    <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started with Hims →</a>
    <a class="btn-outline-white" href="index.html">← All Services</a>
  </div>
</section>
<div class="trust-bar">
  <div class="trust-item"><span>👨‍⚕️</span> Licensed US Providers</div>
  <div class="trust-item"><span>💊</span> Discreet Delivery</div>
  <div class="trust-item"><span>🔒</span> HIPAA Compliant</div>
  <div class="trust-item"><span>⭐</span> 3 Million+ Men Served</div>
</div>
<div class="features">{features_html}</div>
{faq_html}
<div class="related">
  <div class="sec-title">Related Services</div>
  <div class="rel-grid">{related_html}</div>
</div>
<section class="cta-band">
  <h2>{cta_h2}</h2>
  <p>{cta_p}</p>
  <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Start with Hims Today →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">💊 Get Started</a>
<footer>
  © {YEAR} Hims Affiliate Guide · <a href="index.html">Home</a> · Affiliate links used · Individual results may vary · Not medical advice
</footer>
</body>
</html>"""

def make_faq(faqs):
    if not faqs: return ""
    items = "".join(
        f'<div class="faq-item"><div class="faq-q">❓ {q}</div><div class="faq-a">Hims connects you with licensed US providers who can evaluate and address this. Visit Hims to get started with a free online assessment.</div></div>'
        for q in faqs
    )
    return f'<div class="faq-section"><div class="faq-title">Frequently Asked Questions</div>{items}</div>'

# ── STATE PAGES ───────────────────────────────────────────────────────────────
def make_state_page(st_slug, st_name, st_abbr, i_slug, i_name, i_kw):
    slug  = f"hims-{st_slug}-{i_slug}.html"
    title = f"Hims {i_name} in {st_name} {YEAR} | Men's Telehealth"
    desc  = f"Get {i_kw} in {st_name} through Hims. Licensed {st_abbr} providers. Prescriptions delivered discreetly to your door. Start your free assessment today."
    h1    = f"👨‍⚕️ Hims {i_name} in {st_name}"
    badge = f"📍 {st_abbr} · Men's Health · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>{st_name} Providers</h3><p>Hims works with licensed healthcare providers in {st_name} ({st_abbr}) to deliver quality men's health care. Free online assessment, fast consultation.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Discreet Delivery</h3><p>Medications prescribed by your Hims provider are shipped discreetly to your {st_name} home. No embarrassing pharmacy trips.</p></div>
<div class="feat"><div class="feat-icon">👨‍⚕️</div><h3>Licensed {st_abbr} Providers</h3><p>All Hims providers are licensed to practice in {st_name}. Same quality care as an in-person visit, from the comfort of home.</p></div>
<div class="feat"><div class="feat-icon">⚡</div><h3>Fast Access in {st_name}</h3><p>Most Hims patients in {st_name} connect with a provider within 24 hours. No waiting rooms, no commute.</p></div>"""
    faqs = [f"Is Hims available in {st_name}?", f"Can Hims prescribe medication to {st_name} residents?", f"How long does delivery take in {st_name}?", "Does Hims accept insurance?"]
    related_html = "".join(
        f'<a href="hims-{s2}-{i_slug}.html" class="rel-card">Hims {sn2} ({sa2})</a>'
        for s2, sn2, sa2 in STATES[:10] if s2 != st_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Ready to Start {i_name} in {st_name}?",
        f"Join millions of men who trust Hims for convenient, discreet healthcare.")

# ── CITY PAGES ────────────────────────────────────────────────────────────────
def make_city_page(c_slug, c_name, c_state, i_slug, i_name, i_kw):
    slug  = f"hims-{c_slug}-{i_slug}.html"
    title = f"Hims {i_name} {c_name}, {c_state} {YEAR} | Men's Telehealth"
    desc  = f"Get {i_kw} in {c_name}, {c_state} through Hims. Licensed providers, discreet prescription delivery, HIPAA-compliant men's healthcare."
    h1    = f"💊 Hims {i_name} — {c_name}, {c_state}"
    badge = f"📍 {c_name}, {c_state} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">🏙️</div><h3>{c_name} Men's Health</h3><p>Hims serves men in {c_name}, {c_state} with convenient online healthcare. No commute, no waiting room — expert care at your door.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Discreet Delivery to {c_name}</h3><p>Prescriptions are shipped discreetly to your {c_name} address. Plain packaging, fast delivery — your privacy protected.</p></div>
<div class="feat"><div class="feat-icon">👨‍⚕️</div><h3>Licensed Providers</h3><p>All Hims providers serving {c_name} are licensed in {c_state}. Expert care without leaving home.</p></div>
<div class="feat"><div class="feat-icon">⚡</div><h3>Same-Day Consultation</h3><p>Most {c_name} patients connect with a Hims provider the same day. Start free and get care within hours.</p></div>"""
    faqs = [f"Is Hims available in {c_name}?", f"How fast can I get a prescription in {c_name}?", f"Does Hims deliver to {c_name}, {c_state}?", "Is Hims covered by insurance?"]
    related_html = "".join(
        f'<a href="hims-{st_slug}-{i_slug}.html" class="rel-card">Hims {st_name} ({st_abbr})</a>'
        for st_slug, st_name, st_abbr in STATES[:10]
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Start Your {i_name} Journey in {c_name}",
        f"Join millions of men who trust Hims for expert, discreet online healthcare.")

# ── SERVICE OVERVIEW ──────────────────────────────────────────────────────────
def make_service_overview(ss, sn, st2, sk, si, sd, sf):
    slug  = f"hims-{ss}-overview.html"
    title = f"Hims {sn} {YEAR} | Complete Guide for Men"
    desc  = f"Complete guide to {sn.lower()} through Hims. {sd[:120]}... Licensed US providers, discreet delivery."
    h1    = f"{si} Hims {sn}: Complete Guide {YEAR}"
    badge = f"✅ {sn} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">{si}</div><h3>What is {sn}?</h3><p>{sd}</p></div>
<div class="feat"><div class="feat-icon">👨‍⚕️</div><h3>How Hims Provides {sn}</h3><p>Complete a free online assessment. A licensed US provider reviews your health history and creates a personalized {sn.lower()} treatment plan.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Discreet Treatment Delivery</h3><p>Your {sn.lower()} medication is shipped discreetly to your US home. Plain packaging, fast delivery, HIPAA-compliant.</p></div>
<div class="feat"><div class="feat-icon">🔄</div><h3>Ongoing Support</h3><p>Hims provides continuous follow-up for {sn.lower()} patients — check ins, dose adjustments, and provider messaging anytime.</p></div>"""
    related_html = "".join(
        f'<a href="hims-{ss2}-overview.html" class="rel-card">{si2} {sn2}</a>'
        for ss2, sn2, st3, sk2, si2, sd2, sf2 in SERVICES if ss2 != ss
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(sf), related_html,
        f"Start {sn} with Hims Today",
        f"Get expert {sn.lower()} care from licensed US providers. Discreet, affordable, and convenient.")

# ── SERVICE INTENT PAGES ──────────────────────────────────────────────────────
def make_service_page(ss, sn, st2, sk, si, sd, sf, i_slug, i_name):
    slug  = f"hims-{ss}-{i_slug}.html"
    title = f"Hims {sn} — {i_name} {YEAR} | Men's Online Healthcare"
    desc  = f"Get {sk} through Hims. {sd[:100]}... Licensed US providers, discreet delivery, fast consultation."
    h1    = f"{si} Hims {sn}: {i_name}"
    badge = f"✅ {sn} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">{si}</div><h3>{sn}</h3><p>{sd}</p></div>
<div class="feat"><div class="feat-icon">👨‍⚕️</div><h3>Expert Provider Evaluation</h3><p>A licensed US provider reviews your medical history and determines if {sn.lower()} treatment is right for you. Fast and confidential.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Discreet Delivery</h3><p>Once prescribed, your {sn.lower()} treatment is shipped discreetly to your US home. Plain packaging, no labels.</p></div>
<div class="feat"><div class="feat-icon">🔄</div><h3>Ongoing Support</h3><p>Hims provides ongoing follow-up care — check ins with your provider, dose adjustments, and messaging anytime.</p></div>"""
    related_html = "".join(
        f'<a href="hims-{ss2}-overview.html" class="rel-card">{si2} {sn2}</a>'
        for ss2, sn2, st3, sk2, si2, sd2, sf2 in SERVICES if ss2 != ss
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(sf), related_html,
        f"Start {sn} with Hims Today",
        f"Get expert {sn.lower()} care from licensed US providers. Discreet, affordable, convenient.")

# ── COMPETITOR PAGES ──────────────────────────────────────────────────────────
def make_competitor_page(c_slug, c_name, c_short, c_type, i_slug, i_name, i_kw):
    slug  = f"hims-vs-{c_slug}-{i_slug}.html"
    title = f"Hims vs {c_name} {YEAR} — {i_name} | Which is Better for Men?"
    desc  = f"Detailed {i_kw} between Hims and {c_name}. Compare cost, services, providers, and user reviews. Find the best men's telehealth platform."
    h1    = f"⚖️ Hims vs {c_name}: {i_name}"
    badge = f"🔍 Comparison · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">👨‍⚕️</div><h3>Hims: Men-First Focus</h3><p>Hims is built specifically for men's health — hair loss, ED, PE, mental health, weight loss, testosterone, and skin care. {c_name} is a {c_type}.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Prescription Services</h3><p>Hims offers prescriptions for hair loss, ED, PE, mental health, weight loss, and skin care. Compare with {c_name}'s {i_kw}.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>Cost Comparison</h3><p>Hims offers competitive pricing for men's telehealth. Compare costs with {c_name} to find the best value.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Why Men Choose Hims</h3><p>3 million+ men trust Hims. Specialized men's care, discreet delivery, and ongoing provider support set Hims apart from {c_name}.</p></div>"""
    faqs = [f"Is Hims better than {c_name} for men?", f"How does Hims compare to {c_name} for hair loss?", f"Which is cheaper, Hims or {c_name}?", f"Does Hims or {c_name} prescribe ED medication?"]
    related_html = "".join(
        f'<a href="hims-vs-{cs2}-{i_slug}.html" class="rel-card">Hims vs {cn2}</a>'
        for cs2, cn2, csh2, ct2 in COMPETITORS if cs2 != c_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Why Choose Hims Over {c_name}?",
        f"Hims is built for men. Get expert care, discreet prescriptions, and ongoing support.")

# ── LONG TAIL PAGES ───────────────────────────────────────────────────────────
def make_longtail_page(lt_slug, lt_name, lt_kw):
    slug  = f"{lt_slug}.html"
    title = f"{lt_name} | Hims Men's Telehealth {YEAR}"
    desc  = f"Complete guide to {lt_kw}. Hims provides licensed US providers, fast prescriptions, and ongoing care for men. Start your free assessment today."
    h1    = f"🔍 {lt_name}"
    badge = f"⭐ {lt_kw.title()} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">🔬</div><h3>Expert Information</h3><p>Everything you need to know about {lt_kw} from licensed healthcare professionals. Evidence-based men's health information.</p></div>
<div class="feat"><div class="feat-icon">👨‍⚕️</div><h3>Licensed Provider Care</h3><p>Hims connects you with licensed US providers who specialize in {lt_kw}. Expert evaluation and personalized treatment plans.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Discreet Prescription Delivery</h3><p>If medication is right for you, your Hims provider will prescribe it and ship it discreetly to your US home.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Trusted by 3M+ Men</h3><p>Hims is America's leading men's telehealth platform. Join 3 million+ men who've transformed their health with Hims.</p></div>"""
    faqs = [f"How does Hims help with {lt_kw}?", "Is Hims covered by insurance?", "How fast can I get treatment through Hims?", "Are Hims providers licensed in my state?"]
    related_html = "".join(
        f'<a href="{ls2}.html" class="rel-card">{ln2}</a>'
        for ls2, ln2, lk2 in LONG_TAILS[:12] if ls2 != lt_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get Expert Care for {lt_name}",
        f"Hims provides licensed US providers for {lt_kw}. Start your free assessment today.")

# ── STATE × SERVICE ───────────────────────────────────────────────────────────
def make_state_service_page(st_slug, st_name, st_abbr, ss, sn, si, sk):
    slug  = f"hims-{st_slug}-{ss}.html"
    title = f"Hims {sn} in {st_name} {YEAR} | Men's Online Health"
    desc  = f"Get {sk} in {st_name} through Hims. Licensed {st_abbr} providers, discreet prescription delivery, HIPAA-compliant men's healthcare."
    h1    = f"{si} Hims {sn} in {st_name}"
    badge = f"📍 {st_abbr} · {sn} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>{sn} in {st_name}</h3><p>Hims provides {sn.lower()} to men throughout {st_name} ({st_abbr}). Licensed local providers, discreet delivery, no embarrassing pharmacy trips.</p></div>
<div class="feat"><div class="feat-icon">{si}</div><h3>Expert {sn}</h3><p>Get specialized {sk} from a licensed {st_abbr} provider. Hims makes it easy to access quality care without leaving home.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Discreet Delivery to {st_name}</h3><p>All prescriptions are shipped discreetly to your {st_name} address. Plain packaging, fast delivery to every city in {st_name}.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>#1 in {st_name}</h3><p>Hims is the leading men's telehealth platform in {st_name}. Trusted by thousands of {st_abbr} men for quality, discreet healthcare.</p></div>"""
    faqs = [f"Does Hims offer {sn.lower()} in {st_name}?", f"How much does Hims {sn.lower()} cost in {st_name}?", f"Is Hims covered by insurance in {st_name}?", f"How fast is delivery in {st_name}?"]
    related_html = "".join(
        f'<a href="hims-{s2}-{ss}.html" class="rel-card">Hims {sn2} {sn}</a>'
        for s2, sn2, sa2 in STATES[:10] if s2 != st_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get {sn} in {st_name} with Hims",
        f"Join {st_name} men who trust Hims for {sn.lower()}. Start your free assessment now.")

# ── INDEX ─────────────────────────────────────────────────────────────────────
def make_index():
    svc_cards = "".join(
        f'<a href="hims-{ss}-overview.html" class="feat" style="cursor:pointer"><div class="feat-icon">{si}</div><h3>{sn}</h3><p>{sd[:80]}...</p></a>'
        for ss, sn, st2, sk, si, sd, sf in SERVICES
    )
    state_cards = "".join(
        f'<a href="hims-{s}-hair-loss-online.html" class="rel-card">📍 {sn} ({sa})</a>'
        for s, sn, sa in STATES
    )
    comp_cards = "".join(
        f'<a href="hims-vs-{cs}-vs.html" class="rel-card">Hims vs {cn}</a>'
        for cs, cn, csh, ct in COMPETITORS
    )
    lt_cards = "".join(
        f'<a href="{ls}.html" class="rel-card">{ln}</a>'
        for ls, ln, lk in LONG_TAILS[:24]
    )
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Hims Men's Telehealth {YEAR} | Hair Loss, ED, PE, Mental Health & More</title>
<meta name="description" content="Hims — America's leading men's telehealth platform. Hair loss, ED, PE, mental health, weight loss, testosterone, skin care and more. Licensed US providers, discreet delivery."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{BASE_URL}"/>
{FONTS}
<style>{CSS}
.section{{max-width:1200px;margin:0 auto;padding:52px 24px}}
.section-title{{font-size:22px;font-weight:800;color:var(--blue);margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid var(--border)}}
.service-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}
</style>
</head>
<body>
<header class="site-header">
  <div class="nav-inner">
    <div class="logo">Hims</div>
    <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started →</a>
  </div>
</header>
<section class="hero">
  <div class="hero-badge">👨‍⚕️ America's #1 Men's Telehealth · {YEAR}</div>
  <h1>Healthcare Built for Men</h1>
  <p>Hair loss, ED, PE, mental health, weight loss, testosterone, skin care — all from licensed US providers, delivered discreetly to your door.</p>
  <div class="cta-group">
    <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Start Free Assessment →</a>
  </div>
</section>
<div class="trust-bar">
  <div class="trust-item"><span>👨‍⚕️</span> Licensed US Providers</div>
  <div class="trust-item"><span>💊</span> Discreet Delivery</div>
  <div class="trust-item"><span>🔒</span> HIPAA Compliant</div>
  <div class="trust-item"><span>⭐</span> 3 Million+ Men Served</div>
  <div class="trust-item"><span>🚀</span> Same-Day Consultations</div>
</div>
<div class="section">
  <div class="section-title">💊 Our Services</div>
  <div class="service-grid">{svc_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">📍 Find Hims by State</div>
  <div class="rel-grid">{state_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">⚖️ Hims vs Competitors</div>
  <div class="rel-grid">{comp_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">🔍 Research Topics</div>
  <div class="rel-grid">{lt_cards}</div>
</div>
<section class="cta-band">
  <h2>Start Your Health Journey with Hims</h2>
  <p>3 million+ men trust Hims. Licensed providers, discreet delivery, affordable care.</p>
  <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started Free →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">💊 Get Started</a>
<footer>© {YEAR} Hims Affiliate Guide · Affiliate links used · Not medical advice · <a href="index.html">Home</a></footer>
</body>
</html>"""

# ── SITEMAP / ROBOTS / LLMS ───────────────────────────────────────────────────
def make_sitemap(urls):
    iso = now.strftime("%Y-%m-%d")
    sm  = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += f'  <url><loc>{BASE_URL}</loc><changefreq>daily</changefreq><priority>1.0</priority><lastmod>{iso}</lastmod></url>\n'
    for url in urls:
        sm += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.7</priority><lastmod>{iso}</lastmod></url>\n'
    sm += '</urlset>\n'
    return sm

def make_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /build.py\nDisallow: /.github/\nCrawl-delay: 1\nSitemap: {BASE_URL}sitemap.xml\n"

def make_llms():
    return f"# Hims Men's Telehealth USA\n> Updated: {DATE_STR}\n> Affiliate links present\n\n## About\n26,000+ page USA affiliate site for Hims men's telehealth.\nCovers all 50 states, 250 cities, 15 services, 20 competitors, 300 long-tail keywords.\nServices: Hair Loss, ED, PE, Mental Health, Weight Loss, Testosterone, Skin Care.\n\n## Site: {BASE_URL}\n"

# ── MAIN ──────────────────────────────────────────────────────────────────────
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout.strip(): print(r.stdout.strip())
    return r.returncode

if __name__ == "__main__":
    state_p = len(STATES) * len(STATE_INTENTS)
    city_p  = len(CITIES) * len(STATE_INTENTS)
    svc_p   = len(SERVICES) * len(STATE_INTENTS[:30]) + len(SERVICES)
    comp_p  = len(COMPETITORS) * len(COMP_INTENTS)
    lt_p    = len(LONG_TAILS)
    ss_p    = len(STATES) * len(SERVICES)
    total   = state_p + city_p + svc_p + comp_p + lt_p + ss_p

    print(f"💊  Hims Build — {DATE_STR}  sync={SYNC}")
    print(f"   State pages:      {state_p:,}")
    print(f"   City pages:       {city_p:,}")
    print(f"   Service pages:    {svc_p:,}")
    print(f"   Competitor pages: {comp_p:,}")
    print(f"   Long-tail pages:  {lt_p:,}")
    print(f"   State×Service:    {ss_p:,}")
    print(f"   Total: {total:,} pages")

    with open("index.html","w",encoding="utf-8") as f: f.write(make_index())
    with open("robots.txt","w",encoding="utf-8") as f: f.write(make_robots())
    with open("llms.txt","w",encoding="utf-8") as f: f.write(make_llms())
    with open(".nojekyll","w") as f: f.write("")
    print("✅ index.html  robots.txt  llms.txt  .nojekyll")

    sitemap_urls = []
    count = 0

    print("   Generating state pages...")
    for st_slug, st_name, st_abbr in STATES:
        for i_slug, i_name, i_kw in STATE_INTENTS:
            slug, html = make_state_page(st_slug, st_name, st_abbr, i_slug, i_name, i_kw)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating city pages...")
    for c_slug, c_name, c_state in CITIES:
        for i_slug, i_name, i_kw in STATE_INTENTS:
            slug, html = make_city_page(c_slug, c_name, c_state, i_slug, i_name, i_kw)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1
            if count % 5000 == 0: print(f"   {count:,}/{total:,}...")

    print("   Generating service pages...")
    for svc in SERVICES:
        ss, sn, st2, sk, si, sd, sf = svc
        slug, html = make_service_overview(ss, sn, st2, sk, si, sd, sf)
        with open(slug,"w",encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1
        for i_slug, i_name, i_kw in STATE_INTENTS[:30]:
            slug, html = make_service_page(ss, sn, st2, sk, si, sd, sf, i_slug, i_name)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating competitor pages...")
    for c_slug, c_name, c_short, c_type in COMPETITORS:
        for i_slug, i_name, i_kw in COMP_INTENTS:
            slug, html = make_competitor_page(c_slug, c_name, c_short, c_type, i_slug, i_name, i_kw)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating long-tail pages...")
    for lt in LONG_TAILS:
        slug, html = make_longtail_page(*lt)
        with open(slug,"w",encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1

    print("   Generating state × service pages...")
    for st_slug, st_name, st_abbr in STATES:
        for ss, sn, st2, sk, si, sd, sf in SERVICES:
            slug, html = make_state_service_page(st_slug, st_name, st_abbr, ss, sn, si, sk)
            with open(slug,"w",encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print(f"✅ {count:,} pages written")
    with open("sitemap.xml","w",encoding="utf-8") as f: f.write(make_sitemap(sitemap_urls))
    print(f"✅ sitemap.xml — {len(sitemap_urls)+1:,} URLs")

    print("\n── Git ──")
    run("git add -A")
    n = int(subprocess.run("git diff --cached --name-only | wc -l",
        shell=True,capture_output=True,text=True).stdout.strip())
    print(f"Staged: {n:,} files")
    if n == 0:
        print("Nothing to commit"); sys.exit(0)
    run(f'git commit -m "hims sync {SYNC}"')
    import time
    for i in range(1,6):
        print(f"Push attempt {i}...")
        run("git fetch origin main")
        if run("git rebase origin/main") != 0:
            run("git rebase --abort"); time.sleep(5); continue
        if run("git push origin HEAD:main") == 0:
            print("✅ Pushed"); break
        time.sleep(5)
    else:
        print("❌ Push failed"); sys.exit(1)
