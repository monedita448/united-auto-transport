B = "https://www.united-autotransport.com/"
Q = B + "get-a-quote.html"
HIW = B + "how-it-works.html"
OPEN = B + "services/open-auto-transport.html"
ENC = B + "services/enclosed-auto-transport.html"
CANY = B + "routes/california-to-new-york-car-shipping.html"
SPEC = B + "index.html#specialized"
LIAB = B + "legal/carrier-liability.html"
CB = B + "index.html#callback"
BLOG = B + "blog/"

CTA_Q = "Free quote: " + Q
CTA_CALL = "Call now / request a callback: " + CB

# (tipo, segmento, kw, kw_sec, titulo, slug, meta, outline, enlaces_internos, cta, fb_ig, gbp, linkedin, email)
DAYS = [
 # ---------------- SEMANA 1 ----------------
 ("Ruta", "Snowbirds (NE → FL)",
  "new york to florida car shipping", "ship car from NY to FL; snowbird car transport; NY to FL auto transport cost",
  "New York to Florida Car Shipping: Snowbird Season Guide (2026)",
  "new-york-to-florida-car-shipping",
  "Shipping a car from New York to Florida this winter? Typical transit times, open vs. enclosed options and how to book early. Get a free quote today.",
  "H2 Why NY→FL is the busiest lane in fall | H2 Typical transit time & distance | H2 Open vs. enclosed for this route | H2 Door-to-door pickup from NYC, Long Island, Upstate | H2 What affects your price (season, vehicle, flexibility) | H2 How to book (step by step) | H2 FAQ | CTA box",
  f"{OPEN}; {ENC}; {HIW}; {Q}", CTA_Q,
  "Heading south for the winter? 🌴 Your car can meet you in Florida. Door-to-door from New York with FMCSA-verified carriers and tracking until delivery. Peak snowbird season fills carrier trucks fast, so lock in your spot now. 👉 Free quote (link in bio) #snowbird #carshipping #florida",
  "Snowbird season is here. We ship cars from New York to Florida door-to-door on open or enclosed carriers, with verified carrier insurance and tracking. Book early for the best pickup dates. Get your free quote today.",
  "", "Asunto: Your car can beat you to Florida this winter 🌴",
 ),
 ("Dealers (pilar)", "Concesionarios",
  "dealer auto transport", "dealership car shipping; dealer vehicle transport services; auto transport for car dealers",
  "Dealer Auto Transport: How Dealerships Move Inventory Faster (Without the Headaches)",
  "dealer-auto-transport",
  "Dealer auto transport for auctions, dealer trades and out-of-state buyers. FMCSA-verified carriers, one contact, fast pickups. Get a dealer quote.",
  "H2 What dealers actually need from a transport partner | H2 Common dealer shipments (auction, trades, retail delivery, wholesale) | H2 Open vs. enclosed for inventory | H2 How carrier vetting works (FMCSA, insurance, BOL) | H2 Volume & recurring lanes | H2 How to start (dealer account) | CTA box",
  f"{HIW}; {LIAB}; {ENC}; {Q}", "Dealer quote / call now: " + CB,
  "Dealers: stop chasing carriers. One call, one contact, FMCSA-verified carriers for auction pickups, dealer trades and out-of-state buyers. 🚚 Request your dealer quote today. #cardealer #autotransport #dealerlife",
  "Car dealers: we move auction purchases, dealer trades and retail deliveries nationwide with FMCSA-verified carriers. Call now to set up your dealer account.",
  "Every day a unit sits at auction or waits on a carrier is a day it isn't on your lot. We handle dealer transport end to end: auction pickups, dealer trades and home delivery for out-of-state buyers, with FMCSA-verified carriers and a single point of contact. If you move more than a few units a month, let's talk about your regular lanes. #DealerOps #AutoTransport",
  "Asunto: Dealers: one call to move your auction and trade units",
 ),
 ("Guía", "Snowbirds",
  "snowbird car shipping", "when to ship car to florida for winter; snowbird auto transport tips",
  "Snowbird Car Shipping: When to Book, What to Expect and How to Save",
  "snowbird-car-shipping-guide",
  "The snowbird car shipping guide: best booking windows, transit times, how to prepare your car and how to avoid peak-season delays. Free quote in minutes.",
  "H2 What snowbird season means for carriers (Oct–Jan south, Mar–May north) | H2 Best time to book | H2 Popular snowbird lanes (NY, NJ, MA, PA, OH, MI → FL/AZ) | H2 Open vs. enclosed for your car | H2 Prep checklist | H2 Round-trip planning (south + spring return) | H2 FAQ | CTA box",
  f"{BLOG}new-york-to-florida-car-shipping; {OPEN}; {HIW}; {Q}", CTA_Q,
  "Snowbird tip ❄️➡️🌞 Book your car shipment 2–3 weeks before you head south. Carrier space on Florida lanes tightens fast from late October. We handle door-to-door pickup + tracking. Free quote 👉 link in bio #snowbirds #floridawinter",
  "Planning your winter move south? Our snowbird guide covers when to book, how to prep your car and what to expect. Free quotes for door-to-door car shipping to Florida and Arizona.",
  "", "Asunto: The snowbird checklist (save this before you go south)",
 ),
 ("Ruta", "Mudanza / costa a costa",
  "california to new york car shipping", "ship car from california to new york cost; cross country car shipping CA to NY; how long to ship a car coast to coast",
  "Shipping a Car from California to New York: Timeline, Options and Tips",
  "california-to-new-york-car-shipping-guide",
  "How long does it take to ship a car from California to New York? Typical 7–10 day transit, open vs. enclosed options and booking tips. Get your free quote.",
  "H2 Coast-to-coast at a glance (~2,800 miles, 7–10 days typical) | H2 Pickup cities (LA, San Diego, Bay Area, Sacramento) | H2 Delivery in NYC vs. Upstate | H2 Weather & mountain passes in winter | H2 When enclosed makes sense | H2 How to book | CTA → route page",
  f"{CANY}; {ENC}; {HIW}; {Q}", CTA_Q,
  "California → New York 🚚 About 2,800 miles, typically 7–10 days door-to-door. Open or enclosed carrier, verified insurance and tracking the whole way. Moving coast to coast? Get your free quote 👉 link in bio #crosscountrymove #carshipping",
  "Moving from California to New York? We ship cars coast to coast door-to-door, typically in 7–10 days. Get a free quote or call now to talk to a specialist.",
  "", "Asunto: Moving coast to coast? Here's your car's timeline",
 ),
 ("Dealers", "Concesionarios / compradores en subasta",
  "auction car transport", "manheim car transport; copart vehicle shipping; auction pickup auto transport",
  "Auction Car Transport: Getting Units from Manheim, ADESA and Copart to Your Lot Fast",
  "auction-car-transport-for-dealers",
  "Bought at auction? We pick up from Manheim, ADESA, Copart and IAA and deliver to your lot. Gate passes, inoperable units, tight storage deadlines handled.",
  "H2 Why auction pickups stall (gate passes, storage fees, release docs) | H2 Auctions we pick up from | H2 Running vs. inoperable units | H2 What the carrier needs from you | H2 Inspection & BOL at pickup | H2 Recurring auction lanes for dealers | CTA box",
  f"{BLOG}dealer-auto-transport; {SPEC}; {HIW}; {Q}", "Dealer quote / call now: " + CB,
  "Won it at auction? Don't let it rack up storage fees. 🏁 We pick up from Manheim, ADESA, Copart & IAA, including non-running units, and deliver to your lot. Dealers, call now. #autoauction #copart #manheim #cardealer",
  "Auction buyers and dealers: we pick up from Manheim, ADESA, Copart and IAA, including inoperable vehicles, and deliver to your lot. Call now for a fast quote.",
  "Storage fees at the auction are pure margin loss. We pick up from Manheim, ADESA, Copart and IAA, running or not, and bring units to your lot with a documented inspection on the BOL at pickup and delivery. Send us your next gate pass. #AutoAuction #UsedCars #DealerOps",
  "Asunto: Stop paying auction storage fees",
 ),
 ("Guía", "Todos (confianza)",
  "open vs enclosed car transport", "is enclosed car shipping worth it; open car carrier vs enclosed",
  "Open vs. Enclosed Car Transport: Which One Do You Actually Need?",
  "open-vs-enclosed-car-transport",
  "Open vs. enclosed car transport compared: protection, availability, cost and which vehicles need enclosed. Make the right choice and get a free quote.",
  "H2 What open transport is | H2 What enclosed transport is | H2 Side-by-side comparison table | H2 When open is the smart choice | H2 When to choose enclosed (classic, exotic, low-clearance, new inventory) | H2 Questions to ask before booking | CTA box",
  f"{OPEN}; {ENC}; {HIW}; {Q}", CTA_Q,
  "Open or enclosed? 🤔 Open = the most common and budget-friendly option. Enclosed = extra protection for classics, exotics and low-clearance cars. Not sure? We'll help you pick. Free quote 👉 link in bio #carshipping #classiccars",
  "Not sure if you need open or enclosed car transport? Open is the most common and economical option; enclosed adds protection for high-value cars. Call now and we'll help you choose.",
  "Dealers moving high-line or new inventory: when does enclosed transport pay for itself? Our quick comparison covers protection, availability and when it's worth it.",
  "Asunto: Open or enclosed? A 2-minute answer",
 ),
 ("Ruta", "Snowbirds (NE → FL)",
  "new jersey to florida car shipping", "ship car NJ to FL; NJ to Florida auto transport",
  "New Jersey to Florida Car Shipping: Door-to-Door for Snowbirds and Movers",
  "new-jersey-to-florida-car-shipping",
  "Ship your car from New Jersey to Florida door-to-door. Typical transit times, pickup tips across NJ, and open or enclosed options. Free quote.",
  "H2 NJ→FL route overview (~1,000–1,200 mi, typical 3–5 days) | H2 Pickup across North, Central & South Jersey | H2 Popular Florida destinations | H2 Booking during peak snowbird weeks | H2 Prep checklist | H2 FAQ | CTA box",
  f"{BLOG}snowbird-car-shipping-guide; {BLOG}new-york-to-florida-car-shipping; {OPEN}; {Q}", CTA_Q,
  "Jersey ➡️ Florida 🌴 Door-to-door car shipping, typically 3–5 days in transit. Verified carriers, tracking and an inspection at pickup and delivery. Book before the holiday rush! Free quote 👉 link in bio #newjersey #snowbird",
  "Shipping a car from New Jersey to Florida? Door-to-door pickup anywhere in NJ, open or enclosed carriers, tracking until delivery. Get your free quote today.",
  "", "Asunto: NJ → FL: book before the holiday rush",
 ),
 # ---------------- SEMANA 2 ----------------
 ("Dealers", "Concesionarios",
  "dealer trade transport", "dealer to dealer car transport; dealer swap shipping",
  "Dealer-to-Dealer Transfers: How to Ship Trades and Swaps Without Losing the Deal",
  "dealer-to-dealer-car-transport",
  "Dealer trades move fast, and your transport should too. How to ship dealer-to-dealer swaps quickly, with inspections and BOL documentation. Call now.",
  "H2 Why trades fall apart (timing) | H2 Same-week dealer trade pickups | H2 Documentation: BOL & condition report | H2 One-way vs. swap logistics | H2 Expedited options | CTA box",
  f"{BLOG}dealer-auto-transport; {SPEC}; {Q}", "Dealer quote / call now: " + CB,
  "Dealer trade on the line? ⏱️ We move dealer-to-dealer swaps fast, with a condition report on the BOL at both ends. Dealers, call now. #cardealer #dealertrade",
  "Dealer-to-dealer trades shipped fast, with documented inspections at pickup and delivery. Call now to move your next trade.",
  "A customer wants the exact trim another store has, and the clock starts. Our dealer-to-dealer transfer process covers pickup timing, condition reports on the BOL and expedited options when the deal can't wait.",
  "Asunto: Close the trade before the customer cools off",
 ),
 ("Ruta", "Mudanza",
  "texas to california car shipping", "ship car from Texas to California; Dallas to LA car transport; Houston to California auto transport",
  "Texas to California Car Shipping: Dallas, Houston, Austin to LA and the Bay Area",
  "texas-to-california-car-shipping",
  "Ship a car from Texas to California door-to-door. Typical transit times from Dallas, Houston and Austin, open vs. enclosed, and how to book. Free quote.",
  "H2 Route overview & typical transit | H2 Pickup metros (DFW, Houston, Austin, San Antonio) | H2 Delivery to SoCal vs. NorCal | H2 Desert heat & your car | H2 Cost factors | H2 FAQ | CTA box",
  f"{OPEN}; {HIW}; {Q}", CTA_Q,
  "Texas ➡️ California 🌵🌉 Door-to-door from DFW, Houston, Austin & San Antonio to LA, San Diego and the Bay Area. Free quote 👉 link in bio #texas #california #carshipping",
  "Moving from Texas to California? We ship cars door-to-door from every major Texas metro. Get a free quote today.",
  "", "Asunto: Texas → California, without the 1,400-mile drive",
 ),
 ("Guía", "Todos (confianza)",
  "bill of lading car shipping", "what is a BOL auto transport; car shipping inspection report",
  "What Is a Bill of Lading (BOL) in Car Shipping, and Why It Protects You",
  "bill-of-lading-car-shipping",
  "The Bill of Lading (BOL) is your car's condition record. What it includes, how to inspect at pickup and delivery, and what to do if there's damage.",
  "H2 BOL in plain English | H2 What's on it | H2 Pickup inspection: step by step | H2 Delivery inspection: what to check before signing | H2 If you find damage | H2 Photos & documentation tips | CTA box",
  f"{LIAB}; {HIW}; {Q}", CTA_CALL,
  "📋 Before you sign the BOL at delivery: walk around the car, compare it to the pickup report, note anything new BEFORE signing. Save this! #carshipping #autotransporttips",
  "Shipping a car? Your Bill of Lading (BOL) documents the condition at pickup and delivery. Read our quick guide and ship with confidence.",
  "Dealers: a clean BOL process protects your margin. A quick refresher on inspections at pickup and delivery and how to document damage claims correctly.",
  "Asunto: The one document that protects your car in transit",
 ),
 ("Ruta", "Snowbirds (NE → FL)",
  "boston to florida car shipping", "massachusetts to florida car shipping; ship car MA to FL",
  "Massachusetts to Florida Car Shipping: Boston Snowbirds' Guide",
  "massachusetts-to-florida-car-shipping",
  "Ship your car from Boston and Massachusetts to Florida door-to-door. Typical transit times, best booking windows and open vs. enclosed. Free quote.",
  "H2 Route overview (~1,250–1,500 mi) | H2 Pickup tips for Boston & tight streets | H2 Destinations (Naples, Sarasota, Palm Beach, Orlando) | H2 Booking windows | H2 FAQ | CTA box",
  f"{BLOG}snowbird-car-shipping-guide; {ENC}; {Q}", CTA_Q,
  "Boston ➡️ Florida 🦞🌴 Skip the I-95 drive. Door-to-door car shipping for Massachusetts snowbirds. Free quote 👉 link in bio #boston #snowbird",
  "Massachusetts snowbirds: we ship your car to Florida door-to-door so you can fly down. Get a free quote today.",
  "", "Asunto: Fly south, we'll bring the car",
 ),
 ("Dealers", "Concesionarios / ventas online",
  "car shipping for online car sales", "ship car to out of state buyer; dealer home delivery shipping",
  "Selling to Out-of-State Buyers? A Dealer's Guide to Home Delivery Shipping",
  "dealer-home-delivery-out-of-state-buyers",
  "Close more out-of-state and online sales with reliable door-to-door delivery. How dealers quote shipping into the deal and keep buyers updated. Dealer quote.",
  "H2 Why shipping closes remote deals | H2 Quoting transport into the deal | H2 Door-to-door delivery experience | H2 Keeping the buyer updated (tracking) | H2 Delivery inspection & BOL with the buyer | H2 Set up a dealer account | CTA box",
  f"{BLOG}dealer-auto-transport; {BLOG}bill-of-lading-car-shipping; {HIW}; {Q}", "Dealer quote / call now: " + CB,
  "Dealers 📲 Your next buyer might be 1,000 miles away. We deliver door-to-door so you can close remote deals with confidence. Call now. #cardealer #onlinecarsales",
  "Dealers: close out-of-state sales with door-to-door delivery to your buyer's driveway. Call now to set up dealer shipping.",
  "Online and out-of-state buyers are now a normal part of the mix. The dealers winning those deals give a confident delivery date up front. Here's how to build transport into the deal without eating your gross.",
  "Asunto: Sell to buyers 1,000 miles away",
 ),
 ("Ruta", "Snowbirds (Midwest → FL)",
  "michigan to florida car shipping", "ohio to florida car shipping; ship car from Detroit to Florida",
  "Michigan and Ohio to Florida Car Shipping: A Midwest Snowbird Guide",
  "michigan-ohio-to-florida-car-shipping",
  "Midwest snowbirds: ship your car from Michigan or Ohio to Florida door-to-door. Typical transit, winter pickup tips and booking advice. Free quote.",
  "H2 Midwest→FL lanes overview | H2 Pickup in snow season | H2 Typical transit | H2 Destinations | H2 Round-trip planning for spring | H2 FAQ | CTA box",
  f"{BLOG}snowbird-car-shipping-guide; {OPEN}; {Q}", CTA_Q,
  "Michigan & Ohio ➡️ Florida ❄️➡️☀️ Leave the snow, not your car. Door-to-door car shipping for Midwest snowbirds. Free quote 👉 link in bio #michigan #ohio #snowbird",
  "Michigan and Ohio snowbirds: door-to-door car shipping to Florida with verified carriers. Get your free quote today.",
  "", "Asunto: Leave the snow behind, not your car",
 ),
 ("Segmento", "Militares PCS",
  "PCS car shipping", "military car shipping; shipping POV PCS move",
  "PCS Car Shipping: Moving Your Vehicle on Military Orders (Stateside)",
  "pcs-military-car-shipping",
  "Got PCS orders? How to ship your car between duty stations in the U.S., with timing, paperwork and door-to-door options. Get a free quote.",
  "H2 Stateside PCS & your POV | H2 When to book after orders | H2 Pickup/delivery near bases | H2 What to have ready | H2 Shipping a second vehicle | H2 FAQ | CTA box",
  f"{HIW}; {OPEN}; {Q}", CTA_Q,
  "🇺🇸 PCS orders? We'll handle the car. Door-to-door shipping between duty stations, verified carriers and tracking. Free quote 👉 link in bio #PCS #militarylife #militaryspouse",
  "Military families: got PCS orders? We ship vehicles between duty stations door-to-door. Get a free quote today.",
  "", "Asunto: PCS orders? Check the car off your list",
 ),
 # ---------------- SEMANA 3 ----------------
 ("Dealers", "Concesionarios",
  "auto transport company for dealerships", "best car transport for dealers; how to choose dealer shipping partner",
  "9 Questions to Ask Before Choosing an Auto Transport Partner for Your Dealership",
  "choose-auto-transport-partner-dealership",
  "Not all auto transport companies are built for dealers. Ask these 9 questions on carrier vetting, insurance, pickup windows and claims first.",
  "H2 1 How are carriers vetted? | H2 2 Insurance verification | H2 3 Pickup windows | H2 4 Single point of contact | H2 5 Inoperable units | H2 6 Enclosed capacity | H2 7 Tracking | H2 8 Claims process | H2 9 Volume pricing | CTA box",
  f"{BLOG}dealer-auto-transport; {LIAB}; {HIW}; {Q}", "Dealer quote / call now: " + CB,
  "Dealers: before you hire a transport company, ask these 9 questions. ✅ Swipe through ➡️ #cardealer #autotransport",
  "Choosing a transport partner for your dealership? Ask these 9 questions first. We're happy to answer all of them. Call now.",
  "Most dealer transport problems are visible before the first load: vague carrier vetting, no single contact, slow claims. 9 questions to ask any auto transport partner, including us.",
  "Asunto: 9 questions to ask your transport company",
 ),
 ("Ruta", "Snowbirds (NE → FL)",
  "pennsylvania to florida car shipping", "philadelphia to florida car shipping; pittsburgh to florida car transport",
  "Pennsylvania to Florida Car Shipping: Philadelphia, Pittsburgh and Beyond",
  "pennsylvania-to-florida-car-shipping",
  "Ship your car from Pennsylvania to Florida door-to-door. Pickup from Philly, Pittsburgh and the Lehigh Valley, typical transit and booking tips. Free quote.",
  "H2 Route overview | H2 Pickup across PA | H2 Transit expectations | H2 Open vs. enclosed | H2 FAQ | CTA box",
  f"{BLOG}snowbird-car-shipping-guide; {BLOG}open-vs-enclosed-car-transport; {Q}", CTA_Q,
  "Pennsylvania ➡️ Florida 🌴 Door-to-door from Philly, Pittsburgh and everywhere in between. Free quote 👉 link in bio #pennsylvania #snowbird",
  "Pennsylvania to Florida car shipping, door-to-door. Get a free quote today.",
  "", "Asunto: PA → FL, door to door",
 ),
 ("Ruta", "Mudanza",
  "california to texas car shipping", "ship car from LA to Dallas; california to austin car shipping",
  "California to Texas Car Shipping: What to Expect When You Move to the Lone Star State",
  "california-to-texas-car-shipping",
  "Moving from California to Texas? Typical transit to Dallas, Austin and Houston, open vs. enclosed options and how to book door-to-door. Free quote.",
  "H2 Why CA→TX is one of the busiest relocation lanes | H2 Transit expectations | H2 Pickup metros | H2 Delivery metros | H2 Registering your car in Texas (overview) | H2 FAQ | CTA box",
  f"{BLOG}texas-to-california-car-shipping; {OPEN}; {Q}", CTA_Q,
  "California ➡️ Texas 🤠 Making the move? Your car can ship door-to-door to Dallas, Austin, Houston or San Antonio. Free quote 👉 link in bio #movingtotexas",
  "Moving from California to Texas? Door-to-door car shipping to every major Texas metro. Free quote today.",
  "", "Asunto: Moving to Texas? Let's ship the car",
 ),
 ("Dealers", "Concesionarios lujo/exóticos",
  "enclosed transport for dealerships", "exotic car dealer transport; luxury car shipping dealers",
  "Enclosed Transport for Luxury and Exotic Dealers: Protecting High-Value Inventory",
  "enclosed-transport-luxury-exotic-dealers",
  "Luxury and exotic dealers: when to use enclosed transport, liftgate loading for low-clearance cars and how to protect high-value inventory in transit.",
  "H2 Why high-line inventory needs enclosed | H2 Soft-tie & liftgate loading | H2 Delivering to VIP buyers | H2 Documentation & photos | H2 Scheduling enclosed capacity | CTA box",
  f"{ENC}; {BLOG}open-vs-enclosed-car-transport; {Q}", "Dealer quote / call now: " + CB,
  "Exotic inventory deserves an enclosed trailer. 🏎️ Liftgate loading, soft ties, door-to-door delivery to your buyer. Dealers, call now. #exoticcars #luxurycars",
  "Luxury and exotic dealers: enclosed transport with liftgate loading for high-value inventory. Call now.",
  "When the unit is a six-figure car, the delivery is part of the sale. How luxury and exotic dealers use enclosed transport to protect inventory and impress the buyer.",
  "Asunto: Protect your six-figure inventory",
 ),
 ("Ruta", "Snowbirds (→ AZ)",
  "car shipping to arizona", "new york to arizona car shipping; ship car to scottsdale for winter",
  "Shipping Your Car to Arizona for the Winter: A Snowbird's Guide",
  "snowbird-car-shipping-to-arizona",
  "Wintering in Phoenix, Scottsdale or Tucson? How to ship your car to Arizona door-to-door, typical transit and when to book. Get a free quote.",
  "H2 Arizona snowbird season | H2 Common origins (NY, IL, MN, WA) | H2 Typical transit | H2 Destinations | H2 Booking tips | H2 FAQ | CTA box",
  f"{BLOG}snowbird-car-shipping-guide; {HIW}; {Q}", CTA_Q,
  "Wintering in Arizona? 🌵☀️ We'll get your car to Phoenix, Scottsdale or Tucson door-to-door. Free quote 👉 link in bio #arizona #snowbird",
  "Snowbirds headed to Arizona: door-to-door car shipping to Phoenix, Scottsdale and Tucson. Free quote today.",
  "", "Asunto: Arizona winter? Your car's covered",
 ),
 ("Guía", "Todos",
  "how to prepare car for transport", "car shipping checklist; prepare vehicle for auto transport",
  "How to Prepare Your Car for Transport: The 10-Step Checklist",
  "how-to-prepare-car-for-transport",
  "Get your car ready for shipping in 10 steps: clean it, document it, remove personal items, check the battery and more. Free printable checklist inside.",
  "H2 Wash & photograph | H2 Remove personal items | H2 Fuel level | H2 Battery, tires, leaks | H2 Toll tags & alarms | H2 Keys | H2 Fold mirrors/antenna | H2 Note existing damage | H2 Be present for pickup inspection | H2 Check the BOL | CTA box",
  f"{BLOG}bill-of-lading-car-shipping; {HIW}; {Q}", CTA_Q,
  "✅ Car shipping checklist: wash it, photo it, empty it, ~1/4 tank, disable toll tags, be there for the inspection. Save & share! #carshipping #movingtips",
  "Shipping your car soon? Follow our 10-step prep checklist for a smooth pickup. Free quote anytime.",
  "", "Asunto: Your 10-step car shipping checklist",
 ),
 ("Ruta", "Mudanza / snowbirds",
  "texas to florida car shipping", "houston to florida car shipping; dallas to orlando car transport",
  "Texas to Florida Car Shipping: Houston, Dallas and Austin to the Sunshine State",
  "texas-to-florida-car-shipping",
  "Ship your car from Texas to Florida door-to-door. Typical transit from Houston, Dallas and Austin, open vs. enclosed and booking tips. Free quote.",
  "H2 Route overview (I-10 corridor) | H2 Pickup metros | H2 Destinations | H2 Hurricane season considerations | H2 FAQ | CTA box",
  f"{OPEN}; {Q}", CTA_Q,
  "Texas ➡️ Florida 🌴 Door-to-door along the I-10 corridor. Free quote 👉 link in bio #texas #florida #carshipping",
  "Texas to Florida car shipping, door-to-door from Houston, Dallas, Austin and San Antonio. Free quote today.",
  "", "Asunto: Texas → Florida, handled",
 ),
 # ---------------- SEMANA 4+ ----------------
 ("Dealers", "Concesionarios",
  "dealer inventory transport", "year end dealer inventory; Q4 auto transport planning",
  "Q4 Inventory Moves: A Year-End Transport Plan for Dealers",
  "q4-dealer-inventory-transport-plan",
  "Year-end is the busiest time to move dealer inventory. Plan Q4 auction runs, aged-unit transfers and holiday deliveries before carrier capacity tightens.",
  "H2 Why carrier capacity tightens Nov–Dec | H2 Aged inventory transfers | H2 Holiday retail deliveries | H2 Weather & northern routes | H2 Building a weekly transport schedule | CTA box",
  f"{BLOG}dealer-auto-transport; {BLOG}auction-car-transport-for-dealers; {Q}", "Dealer quote / call now: " + CB,
  "Dealers 📆 Year-end + snowbird season = tight carrier capacity. Lock in your Q4 transport plan now. Call us. #cardealer #Q4",
  "Dealers: plan your year-end inventory moves before carrier capacity tightens. Call now for a dealer quote.",
  "Q4 is when snowbird traffic, holiday deliveries and year-end inventory pushes all compete for the same trucks. A simple plan to keep units moving through December.",
  "Asunto: Your Q4 transport plan (before trucks fill up)",
 ),
 ("Ruta", "Mudanza costa a costa",
  "california to florida car shipping", "ship car from LA to Miami; cross country car shipping to Florida",
  "California to Florida Car Shipping: Coast-to-Coast Guide",
  "california-to-florida-car-shipping",
  "Shipping a car from California to Florida? Typical coast-to-coast transit, open vs. enclosed and how to book door-to-door. Get a free quote.",
  "H2 Route overview (~2,500–2,800 mi) | H2 Typical transit | H2 Pickup & delivery metros | H2 Open vs. enclosed | H2 FAQ | CTA box",
  f"{BLOG}california-to-new-york-car-shipping-guide; {ENC}; {Q}", CTA_Q,
  "California ➡️ Florida 🌉➡️🌴 Coast to coast, door-to-door. Free quote 👉 link in bio #crosscountry #carshipping",
  "Coast-to-coast car shipping from California to Florida. Door-to-door, open or enclosed. Free quote today.",
  "", "Asunto: Coast to coast, door to door",
 ),
 ("Guía", "Todos",
  "cost to ship a car across country", "how much does it cost to ship a car; car shipping price factors",
  "How Much Does It Cost to Ship a Car Across the Country? (What Really Moves the Price)",
  "cost-to-ship-a-car-across-country",
  "What drives the cost to ship a car across the country: distance, vehicle size, open vs. enclosed, season and flexibility. Get your exact price free.",
  "H2 The main price factors | H2 Distance & route popularity | H2 Vehicle size & condition | H2 Open vs. enclosed | H2 Season (snowbird peak) | H2 Flexibility saves money | H2 Red flags: too-low quotes | CTA box",
  f"{BLOG}open-vs-enclosed-car-transport; {CANY}; {Q}", CTA_Q,
  "💲 What really sets your car shipping price? Distance, vehicle size, open vs. enclosed, season and pickup flexibility. Get your real price free 👉 link in bio #carshipping",
  "Wondering what it costs to ship your car? Price depends on route, vehicle, carrier type and season. Get your exact free quote today.",
  "", "Asunto: What really sets your car shipping price",
 ),
 ("Dealers", "Concesionarios / subastas",
  "inoperable vehicle transport", "non running car shipping; ship car that doesn't run",
  "Inoperable Vehicle Transport: Shipping Non-Running Cars for Dealers and Auction Buyers",
  "inoperable-vehicle-transport",
  "Need to ship a car that doesn't run? How inoperable vehicle transport works: winch-equipped carriers, what to disclose and pickup tips. Get a quote.",
  "H2 What counts as inoperable | H2 Winch & forklift loading | H2 Disclosing condition correctly | H2 Auction salvage units | H2 Timing | CTA box",
  f"{SPEC}; {BLOG}auction-car-transport-for-dealers; {Q}", "Dealer quote / call now: " + CB,
  "Doesn't run? Still ships. 🔧 Winch-equipped carriers for non-running units, from auctions, shops or driveways. Call now. #salvagecars #copart",
  "We ship inoperable and non-running vehicles with winch-equipped carriers. Dealers and auction buyers, call now.",
  "Non-running units from auctions are a routine part of used inventory, but they need the right truck. What to disclose and how to avoid failed pickups.",
  "Asunto: Non-running units? We ship those too",
 ),
 ("Ruta", "Snowbirds (Midwest → AZ/FL)",
  "illinois to arizona car shipping", "chicago to phoenix car shipping; chicago to florida car shipping",
  "Chicago to Arizona and Florida Car Shipping: Illinois Snowbirds' Guide",
  "chicago-to-arizona-florida-car-shipping",
  "Illinois snowbirds: ship your car from Chicago to Arizona or Florida door-to-door. Typical transit, booking windows and tips. Free quote.",
  "H2 Two favorite winter destinations | H2 Chicago pickup tips | H2 Transit expectations | H2 Booking tips | H2 FAQ | CTA box",
  f"{BLOG}snowbird-car-shipping-to-arizona; {BLOG}snowbird-car-shipping-guide; {Q}", CTA_Q,
  "Chicago ➡️ Phoenix or Florida? ❄️➡️☀️ Door-to-door car shipping for Illinois snowbirds. Free quote 👉 link in bio #chicago #snowbird",
  "Illinois snowbirds: door-to-door car shipping to Arizona and Florida. Free quote today.",
  "", "Asunto: Chicago winter? Not for your car",
 ),
 ("Segmento", "Estudiantes",
  "ship car to college", "college student car shipping; ship car to university",
  "Shipping a Car to College: A Guide for Students and Parents",
  "ship-car-to-college",
  "Sending a car to campus? How students and parents ship a car to college door-to-door, when to book around semester breaks and how to prep. Free quote.",
  "H2 Ship vs. drive | H2 Timing around move-in & breaks | H2 Campus delivery logistics | H2 Prep checklist | H2 FAQ | CTA box",
  f"{BLOG}how-to-prepare-car-for-transport; {OPEN}; {Q}", CTA_Q,
  "🎓 Car headed to campus? Skip the cross-country drive. Door-to-door shipping timed for winter break. Free quote 👉 link in bio #college #collegeparents",
  "Students and parents: ship a car to college door-to-door. Free quote today.",
  "", "Asunto: Car to campus, without the road trip",
 ),
 ("Segmento", "Relocalización corporativa",
  "corporate vehicle relocation", "employee car shipping relocation; corporate relocation auto transport",
  "Corporate Relocation Car Shipping: A Guide for HR and Relocation Managers",
  "corporate-relocation-car-shipping",
  "HR and relocation managers: how to ship employee vehicles door-to-door, simplify billing and keep transferees updated. Request a corporate quote.",
  "H2 Why vehicle shipping matters in relocation | H2 Door-to-door for transferees | H2 Billing & documentation | H2 Multi-vehicle households | H2 Tracking & communication | CTA box",
  f"{HIW}; {LIAB}; {Q}", CTA_CALL,
  "Relocating employees? 🏢 We ship their cars door-to-door so they arrive ready to work. #relocation #HR",
  "HR and relocation teams: door-to-door vehicle shipping for transferring employees. Call now for a corporate quote.",
  "A transferee's car is one of the most stressful parts of a relocation. How HR and mobility teams can hand it off to a transport partner with clear billing and tracking.",
  "Asunto: One less thing for your transferees",
 ),
 ("Dealers", "Concesionarios",
  "expedited car shipping", "fast car shipping for dealers; guaranteed pickup auto transport",
  "Expedited Car Shipping for Dealers: When Speed Pays for Itself",
  "expedited-car-shipping-for-dealers",
  "When a deal can't wait: how expedited car shipping works for dealers, when it's worth the premium and how to request priority pickup. Call now.",
  "H2 What 'expedited' means | H2 When it pays (sold units, trades, aged inventory) | H2 How priority dispatch works | H2 Setting customer expectations | CTA box",
  f"{SPEC}; {BLOG}dealer-to-dealer-car-transport; {Q}", "Dealer quote / call now: " + CB,
  "Sold unit, buyer waiting? ⚡ Expedited shipping gets priority dispatch. Dealers, call now. #cardealer",
  "Need it moved fast? Expedited car shipping with priority dispatch for dealers. Call now.",
  "A sold unit sitting in transit is a deal at risk. When expedited transport pays for itself, and when it doesn't.",
  "Asunto: When a deal can't wait",
 ),
 ("Hub (enlaces)", "Todos",
  "car shipping transit times", "how long does car shipping take; popular car shipping routes",
  "Popular Car Shipping Routes in the U.S. and Typical Transit Times",
  "car-shipping-routes-transit-times",
  "How long does car shipping take? Typical transit times for the most popular U.S. routes: NY to FL, CA to NY, TX to CA and more. Get a free quote.",
  "H2 How transit time is estimated | H2 Table: top routes & typical transit (links to each route post) | H2 What speeds it up or slows it down | H2 Snowbird season effect | CTA box",
  "Enlazar los 13 posts de ruta del mes + " + CANY + "; " + Q, CTA_Q,
  "How long does car shipping take? ⏱️ Our route guide covers NY→FL, CA→NY, TX→CA and more. Link in bio #carshipping",
  "How long does it take to ship a car? See typical transit times on the most popular U.S. routes. Free quote today.",
  "", "Asunto: How long will your car take? (route guide)",
 ),
]

# ---------------- PLAN FESTIVO Q4 (19-nov a 31-dic 2026), días 31-74 ----------------
# Día 31: mié 2026-11-18 (agregado 2026-11-17 para no dejar el día sin post)
DAYS.append(('Ruta', 'Snowbirds (Sur → FL)', 'north carolina to florida car shipping', 'ship car from nc to fl; charlotte to florida auto transport; raleigh to florida car shipping', 'North Carolina to Florida Car Shipping', 'north-carolina-to-florida-car-shipping', 'Shipping a car from North Carolina to Florida? Typical transit time, open vs. enclosed, door-to-door pickup in Charlotte, Raleigh and beyond, and how to book. Free quote.', 'H2 Why NC drivers ship to Florida in winter | H2 Typical transit time | H2 Door-to-door pickup across North Carolina | H2 Open vs. enclosed | H2 How to prepare | H2 How to book before the holidays | H2 FAQ | CTA box', f"{BLOG}snowbird-car-shipping-guide.html; {BLOG}holiday-car-shipping-deadlines-2026.html; {OPEN}; {Q}", CTA_Q, 'North Carolina to Florida this winter? 🌴 Skip the drive down I-95. We ship your car door-to-door with FMCSA-verified carriers. Free quote, link in bio #snowbird #northcarolina #florida', 'Heading from North Carolina to Florida? We ship cars door-to-door from Charlotte, Raleigh, Greensboro and across NC with FMCSA-verified carriers. Get your free quote today.', 'North Carolina to Florida is one of the steadiest snowbird lanes on the East Coast. We put together a guide on typical transit times, door-to-door pickup in Charlotte, Raleigh and beyond, and booking before the holiday weeks fill carrier trucks. #autotransport #snowbirds #carshipping', 'Asunto: North Carolina to Florida? Your car can beat you there'))
Q4 = {}
Q4[31] = {'fecha': '2026-11-18', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Campos vacíos: la rutina diaria los completa con una semana de anticipación.
# Q4[día] = gancho festivo, ugc (video UGC ese día) y social_only (solo redes, sin blog).
# Día 32: jue 2026-11-19
DAYS.append(('Guía', 'Todos', 'holiday car shipping', 'when to book car shipping for christmas; thanksgiving car transport; ship car before holidays', 'Holiday Car Shipping 2026: When to Book for Thanksgiving and Christmas Delivery', 'holiday-car-shipping-deadlines-2026', 'Planning to ship a car for Thanksgiving or Christmas? When to book, how holiday demand affects pickup windows, and how to lock in your date. Free quote.', 'H2 Why holiday weeks fill carrier trucks | H2 When to book for Thanksgiving delivery | H2 When to book for Christmas delivery | H2 What changes during holiday weeks | H2 Open vs. enclosed in winter | H2 How to book in 3 steps | H2 FAQ | CTA box', f'{HIW}; {OPEN}; {ENC}; {Q}', CTA_Q, 'Want your car there for the holidays? 🦃🎄 Holiday weeks fill carrier trucks fast. Book now and lock in your pickup window, door-to-door with FMCSA-verified carriers. 👉 Free quote, link in bio #carshipping #holidaytravel #snowbird', 'Holiday season is the busiest time to ship a car. Book early to lock in your pickup window for Thanksgiving or Christmas delivery. Door-to-door, FMCSA-verified carriers. Get your free quote today.', 'Holiday weeks are the tightest time of year for carrier capacity: snowbird moves, year-end dealer inventory and holiday travel all compete for the same trucks. We put together a simple booking timeline for Thanksgiving and Christmas delivery. #autotransport #logistics #carshipping', 'Asunto: Want your car there for the holidays? Book this week'))
Q4[32] = {'fecha': '2026-11-19', 'gancho': 'Fechas límite festivas', 'ugc': True, 'social_only': False}
# Día 33: vie 2026-11-20
DAYS.append(('Dealers', 'Concesionarios', 'dealer inventory transport black friday', 'year-end dealer car transport; dealership vehicle shipping december; move dealer inventory fast', 'Black Friday to Year-End: How Dealers Keep Inventory Moving', 'black-friday-dealer-inventory-transport', 'Black Friday through December is the busiest stretch for dealers. How to keep inventory, trades and sold units moving with a reliable transport partner.', 'H2 Why Black Friday to year-end strains transport | H2 Sold units to out-of-state buyers | H2 Dealer trades and transfers | H2 Auction pickups in December | H2 Planning a weekly transport schedule | H2 What to expect from a transport partner | H2 FAQ | CTA box', f'{BLOG}dealer-auto-transport.html; {BLOG}q4-dealer-inventory-transport-plan.html; {Q}', CTA_CALL, 'Dealers 🚗 Black Friday to year-end is your busiest stretch. Keep sold units, trades and auction buys moving with one transport partner. Call (972) 833-2614 to set up your dealer account. #cardealer #autotransport', 'Dealers: Black Friday through December is your busiest selling season. We move sold units, dealer trades and auction purchases door-to-door. Call to set up a dealer account.', "From Black Friday to December 31, dealers compete with snowbird and holiday traffic for the same carrier capacity. A weekly transport schedule keeps sold units, trades and auction buys moving. Here's how we plan it with our dealer partners. #cardealers #automotive #logistics", 'Asunto: Black Friday to year-end: keep your inventory moving'))
Q4[33] = {'fecha': '2026-11-20', 'gancho': 'Black Friday / cierre de año', 'ugc': True, 'social_only': False}
# Día 34: sáb 2026-11-21
DAYS.append(('Ruta', 'Snowbirds (Midwest → FL)', 'illinois to florida car shipping', 'chicago to florida auto transport; ship car from illinois to florida; snowbird car shipping illinois', 'Illinois to Florida Car Shipping for Snowbirds', 'illinois-to-florida-car-shipping', 'Shipping a car from Illinois to Florida for the winter? Typical transit time, open vs. enclosed, door-to-door pickup in Chicagoland and how to book. Free quote.', 'H2 Why Illinois snowbirds ship instead of drive | H2 Typical transit time | H2 Pickup across Chicago and Illinois | H2 Open vs. enclosed in winter | H2 How to prepare the car | H2 How to book | H2 FAQ | CTA box', f'{BLOG}chicago-to-arizona-florida-car-shipping.html; {BLOG}snowbird-car-shipping-guide.html; {OPEN}; {Q}', CTA_Q, 'Illinois to Florida this winter? 🌴 Skip the 1,200-mile drive. We ship your car door-to-door with FMCSA-verified carriers. Free quote, link in bio #snowbird #chicago #florida', 'Heading from Illinois to Florida for the winter? We ship cars door-to-door from Chicagoland and across Illinois with FMCSA-verified carriers. Get a free quote today.', 'Illinois snowbirds are booking their Florida moves now. Our new guide covers typical transit from Chicagoland to Florida, open vs. enclosed in winter and how to book before holiday weeks fill carrier trucks. #autotransport #snowbirds #carshipping', 'Asunto: Illinois to Florida this winter? Skip the drive'))
Q4[34] = {'fecha': '2026-11-21', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 35: dom 2026-11-22
DAYS.append(('Segmento', 'Militares', 'military car shipping pcs', 'pcs car shipping december; military holiday leave car transport; ship pov military', 'Military Holiday Leave and PCS Car Shipping', 'military-holiday-pcs-car-shipping', 'PCS orders over the holidays or heading home on leave? How to ship your personal vehicle door-to-door, what documents you need and when to book.', "H2 PCS moves during the holidays | H2 When the government ships your POV and when it doesn't | H2 Shipping a second vehicle | H2 Documents you'll need | H2 Timing around holiday leave | H2 How to book | H2 FAQ | CTA box", f'{BLOG}pcs-military-car-shipping.html; {HIW}; {Q}', CTA_Q, 'PCS orders over the holidays? 🇺🇸 We ship your car door-to-door to your new duty station with FMCSA-verified carriers. Free quote, link in bio #militarylife #pcs #militaryfamily', 'Military families: PCS orders over the holidays? We ship your personal vehicle door-to-door to your new duty station. Get a free quote today.', "PCS orders don't stop for the holidays. For service members shipping a second vehicle or moving around holiday leave, we put together a guide on documents, timing and door-to-door options. #militarylife #pcs #autotransport", "Asunto: PCS over the holidays? We'll move your car"))
Q4[35] = {'fecha': '2026-11-22', 'gancho': 'Licencia navideña / PCS', 'ugc': False, 'social_only': False}
# Día 36: lun 2026-11-23
DAYS.append(('Ruta', 'Snowbirds (NE → AZ)', 'new york to arizona car shipping', 'ship car ny to az; snowbird car shipping arizona; new york to phoenix auto transport', 'New York to Arizona Car Shipping', 'new-york-to-arizona-car-shipping', 'Shipping a car from New York to Arizona for the winter? Typical transit time, open vs. enclosed, door-to-door pickup and how to book early. Free quote.', 'H2 Why New Yorkers winter in Arizona | H2 Typical transit time | H2 Door-to-door pickup in NYC, Long Island and Upstate | H2 Open vs. enclosed | H2 How to prepare | H2 How to book | H2 FAQ | CTA box', f'{BLOG}snowbird-car-shipping-to-arizona.html; {BLOG}new-york-to-florida-car-shipping.html; {OPEN}; {Q}', CTA_Q, 'New York to Arizona this winter? 🌵 Your car can meet you in Phoenix or Scottsdale. Door-to-door with FMCSA-verified carriers. Free quote, link in bio #snowbird #arizona #newyork', 'Wintering in Arizona? We ship cars from New York to Phoenix, Scottsdale and Tucson door-to-door with FMCSA-verified carriers. Free quote today.', "Arizona is a top winter destination for New Yorkers, and it's a long haul. Our guide covers typical transit times, door-to-door pickup in NYC, Long Island and Upstate, and when to book. #autotransport #snowbirds #carshipping", 'Asunto: New York to Arizona? Your car can meet you there'))
Q4[36] = {'fecha': '2026-11-23', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 37: mar 2026-11-24
DAYS.append(('Guía', 'Todos', 'winter car shipping', 'shipping a car in winter; car transport snow delays; how to prepare car for winter shipping', 'Winter Car Shipping: Weather, Delays and How to Prepare', 'winter-car-shipping-tips', 'Shipping a car in winter? How weather affects pickup and delivery, when enclosed transport makes sense, and how to prepare your car. Free quote.', 'H2 How winter weather affects car shipping | H2 Realistic pickup and delivery windows | H2 When to choose enclosed transport | H2 Preparing your car for cold weather | H2 What to check at delivery (Bill of Lading) | H2 FAQ | CTA box', f'{BLOG}how-to-prepare-car-for-transport.html; {BLOG}open-vs-enclosed-car-transport.html; {ENC}; {Q}', CTA_Q, "Shipping your car this winter? ❄️ Snow can shift pickup windows. Here's how to plan, when enclosed makes sense and what to check on the Bill of Lading. Free quote, link in bio #carshipping #winter", 'Shipping a car this winter? Plan for flexible pickup windows, consider enclosed transport for salt and snow, and inspect on the Bill of Lading at delivery. Free quote today.', 'Winter is when pickup windows need the most flexibility. A practical guide on how snow affects car shipping, when enclosed transport makes sense and what to check on the Bill of Lading at delivery. #autotransport #logistics #winter', 'Asunto: Shipping a car this winter? Read this first'))
Q4[37] = {'fecha': '2026-11-24', 'gancho': 'Invierno', 'ugc': True, 'social_only': False}
# Día 38: mié 2026-11-25
DAYS.append(('Guía', 'Todos', 'thanksgiving car shipping', 'car shipping holiday week; auto transport thanksgiving schedule; ship car thanksgiving', 'Car Shipping During Thanksgiving Week: What Changes', 'thanksgiving-week-car-shipping', 'Shipping a car during Thanksgiving week? What changes with carriers, pickups and deliveries over the holiday, and how to keep your dates on track.', 'H2 Do carriers run on Thanksgiving week? | H2 Pickup and delivery around the holiday | H2 Who needs to be there (and the Bill of Lading) | H2 Tips to keep your dates | H2 FAQ | CTA box', f'{BLOG}holiday-car-shipping-deadlines-2026.html; {HIW}; {Q}', CTA_Q, "Shipping a car this Thanksgiving week? 🦃 Carriers keep rolling, but holiday schedules shift. Here's how to keep your dates on track. Free quote, link in bio #thanksgiving #carshipping", 'Shipping a car during Thanksgiving week? Carriers keep running, but plan for holiday schedules and make sure someone can sign the Bill of Lading. Free quote today.', "Carriers keep running through Thanksgiving week, but schedules shift. Here's what changes for pickups and deliveries over the holiday, and how customers can keep their dates on track. #autotransport #logistics #thanksgiving", "Asunto: Shipping a car on Thanksgiving week? Here's what changes"))
Q4[38] = {'fecha': '2026-11-25', 'gancho': 'Semana de Thanksgiving', 'ugc': False, 'social_only': False}
# Día 39: jue 2026-11-26
DAYS.append(('Social festivo', 'Todos', 'thanksgiving car shipping', 'happy thanksgiving auto transport; car shipping thank you', 'Happy Thanksgiving from United Auto Transport', 'happy-thanksgiving-2026', 'Happy Thanksgiving from United Auto Transport. Thank you to our customers and to the carrier drivers on the road this holiday. Free quote.', 'Social only: thank-you post for customers and carrier drivers | soft free-quote CTA', 'https://www.united-autotransport.com/get-a-quote.html', CTA_Q, "Happy Thanksgiving! 🦃 Thank you for trusting us with your cars this year, and thank you to every carrier driver on the road this holiday. Planning a move after the holiday? Free quote, link in bio #thanksgiving #grateful #carshipping", 'Happy Thanksgiving from United Auto Transport. Thank you to our customers and to the carrier drivers on the road this week. Planning a move? Get a free quote.', 'Happy Thanksgiving from United Auto Transport. This season we are grateful for the customers who trust us with their vehicles and for the carrier drivers who keep cars moving through the holidays. #thanksgiving #autotransport #gratitude', 'Asunto: Happy Thanksgiving from United Auto Transport'))
Q4[39] = {'fecha': '2026-11-26', 'gancho': 'Thanksgiving (26-nov)', 'ugc': True, 'social_only': True}
# Día 40: vie 2026-11-27
DAYS.append(('Segmento', 'Compradores online', 'ship a car bought online', 'ship car bought out of state; black friday car deal shipping; ship car from dealer to home', 'Bought a Car on Black Friday? How to Ship It Home', 'ship-car-bought-black-friday', 'Bought a car online or out of state on Black Friday? How to ship it home door-to-door, what to ask the dealer, the documents you need and how to inspect it on the BOL.', 'H2 Why Black Friday buyers ship instead of drive | H2 Coordinate pickup with the selling dealer | H2 Documents and keys | H2 Open vs. enclosed for a new car | H2 Inspecting at delivery on the Bill of Lading | H2 How to book | H2 FAQ | CTA box', 'https://www.united-autotransport.com/blog/dealer-home-delivery-out-of-state-buyers.html; https://www.united-autotransport.com/blog/bill-of-lading-car-shipping.html; https://www.united-autotransport.com/blog/open-vs-enclosed-car-transport.html; https://www.united-autotransport.com/get-a-quote.html', 'Free quote: https://www.united-autotransport.com/get-a-quote.html', "Scored a Black Friday deal out of state? 🛒🚗 Skip the long drive home. We pick up at the dealer and deliver door-to-door with FMCSA-verified carriers. Free quote, link in bio #blackfriday #newcar #carshipping", 'Bought a car out of state on Black Friday? We pick it up at the dealer and deliver it to your door with FMCSA-verified carriers. Get your free quote today.', "Black Friday car deals often mean buying out of state. Our guide walks buyers through shipping the car home: coordinating pickup with the selling dealer, documents, open vs. enclosed and inspecting on the Bill of Lading. #autotransport #blackfriday #carbuying", 'Asunto: Bought a car on Black Friday? Ship it home door-to-door'))
Q4[40] = {'fecha': '2026-11-27', 'gancho': 'Black Friday (27-nov)', 'ugc': True, 'social_only': False}
# Día 41: sáb 2026-11-28
DAYS.append(('Ruta', 'Snowbirds (NE → FL)', 'connecticut to florida car shipping', 'ship car from connecticut to florida; ct to fl auto transport; snowbird car shipping connecticut', 'Connecticut to Florida Car Shipping', 'connecticut-to-florida-car-shipping', 'Shipping a car from Connecticut to Florida for the winter? Typical transit time, door-to-door pickup across Connecticut, open vs. enclosed and how to book. Free quote.', 'H2 Why Connecticut snowbirds ship instead of drive | H2 Typical transit time | H2 Door-to-door pickup across Connecticut | H2 Open vs. enclosed in winter | H2 How to prepare | H2 How to book | H2 FAQ | CTA box', 'https://www.united-autotransport.com/blog/new-york-to-florida-car-shipping.html; https://www.united-autotransport.com/blog/massachusetts-to-florida-car-shipping.html; https://www.united-autotransport.com/blog/snowbird-car-shipping-guide.html; https://www.united-autotransport.com/get-a-quote.html', 'Free quote: https://www.united-autotransport.com/get-a-quote.html', "Connecticut to Florida this winter? 🌴 Skip I-95 traffic. We ship your car door-to-door with FMCSA-verified carriers. Free quote, link in bio #snowbird #connecticut #florida", 'Heading from Connecticut to Florida for the winter? We ship cars door-to-door from anywhere in Connecticut with FMCSA-verified carriers. Get a free quote today.', "Connecticut snowbirds are booking Florida moves for December. Our guide covers typical transit times on the I-95 corridor, door-to-door pickup across Connecticut and how to book before holiday weeks fill carrier trucks. #autotransport #snowbirds #carshipping", 'Asunto: Connecticut to Florida? Ship your car, skip I-95'))
Q4[41] = {'fecha': '2026-11-28', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 42: dom 2026-11-29
DAYS.append(('Segmento', 'Estudiantes', 'ship car home from college', 'ship car home for winter break; college car shipping december; student car transport holidays', 'Shipping a Car Home for Winter Break', 'ship-car-home-winter-break', 'College student heading home for winter break? How to ship your car home door-to-door, when to book around finals and the holidays, and how to prep. Free quote.', 'H2 Why students ship instead of drive home | H2 When to book around finals and holidays | H2 Pickup on or near campus | H2 Leave it home or ship it back in January | H2 How to prepare the car | H2 FAQ | CTA box', f'{BLOG}ship-car-to-college.html; {BLOG}how-to-prepare-car-for-transport.html; {Q}', CTA_Q, '🎓 Finals done, heading home for winter break? Skip the long drive. We ship your car door-to-door from campus with FMCSA-verified carriers. Free quote, link in bio #college #winterbreak #collegeparents', 'Students and parents: ship a car home for winter break, door-to-door from campus with FMCSA-verified carriers. Book early around finals and the holidays. Get a free quote today.', 'Winter break is a common time for college families to move a car home, and it overlaps with the busiest holiday weeks for carrier capacity. Our guide covers when to book around finals, campus pickup and whether to ship the car back in January. #autotransport #college #carshipping', 'Asunto: Heading home for winter break? Ship the car, skip the drive'))
Q4[42] = {'fecha': '2026-11-29', 'gancho': 'Vacaciones de invierno', 'ugc': False, 'social_only': False}
# Día 43: lun 2026-11-30
DAYS.append(('Segmento', 'Compradores online', 'ship a car bought online out of state', 'how to ship a car you bought online; ship car from private seller; cyber monday car purchase shipping', 'How to Ship a Car You Bought Online From Out of State', 'ship-car-bought-online-out-of-state', 'Bought a car online from an out-of-state dealer or private seller? How to ship it home door-to-door, who releases the car, the documents you need and how to inspect it on the BOL.', 'H2 Buying a car online from another state | H2 Dealer vs. private seller: who releases the car | H2 Documents, keys and payment before pickup | H2 Open vs. enclosed | H2 Inspecting at delivery on the Bill of Lading | H2 How to book | H2 FAQ | CTA box', f'{BLOG}ship-car-bought-black-friday.html; {BLOG}bill-of-lading-car-shipping.html; {HIW}; {Q}', CTA_Q, 'Bought a car online from another state? 💻🚗 We pick it up from the dealer or private seller and deliver it door-to-door with FMCSA-verified carriers. Free quote, link in bio #cybermonday #carbuying #carshipping', 'Bought a car online from out of state? We pick it up from the dealer or private seller and deliver it to your door with FMCSA-verified carriers. Get your free quote today.', 'More buyers are purchasing cars online from dealers and private sellers in other states. Our guide covers who releases the car at pickup, the documents to have ready and how to inspect it on the Bill of Lading at delivery. #autotransport #carbuying #ecommerce', 'Asunto: Bought a car online? Here is how to get it home'))
Q4[43] = {'fecha': '2026-11-30', 'gancho': 'Cyber Monday (30-nov)', 'ugc': True, 'social_only': False}
# Día 44: mar 2026-12-01
DAYS.append(('Dealers', 'Concesionarios', 'dealer inventory transfer transport', 'aged inventory transfer between dealerships; year-end dealer trade transport; move aged units december', 'Year-End Aged Inventory Transfers for Dealers', 'dealer-year-end-inventory-transfers', 'Moving aged units to a sister store or a dealer trade before December 31? How to plan year-end inventory transfers with a reliable carrier partner. Call to set up a dealer account.', 'H2 Why aged inventory moves in December | H2 Sister-store transfers and dealer trades | H2 Planning transfers before the holiday weeks | H2 Paperwork, keys and release | H2 Condition reports on the Bill of Lading | H2 What to expect from a transport partner | H2 FAQ | CTA box', f'{BLOG}dealer-to-dealer-car-transport.html; {BLOG}black-friday-dealer-inventory-transport.html; {BLOG}q4-dealer-inventory-transport-plan.html; {Q}', CTA_CALL, 'Dealers 📦 Aged units sitting on the lot? Move them to a sister store or close that dealer trade before year-end. Door-to-door with FMCSA-verified carriers. Call (972) 833-2614 to set up your dealer account. #cardealer #autotransport', 'Dealers: move aged inventory to sister stores or complete dealer trades before December 31. Door-to-door with FMCSA-verified carriers. Call to set up a dealer account.', "December is when dealers rebalance aged inventory between rooftops and close out dealer trades. Planning those transfers before the holiday weeks fill carrier trucks keeps units selling instead of sitting. Here's how we plan year-end transfers with dealer partners. #cardealers #automotive #logistics", 'Asunto: Aged units on the lot? Move them before year-end'))
Q4[44] = {'fecha': '2026-12-01', 'gancho': 'Cierre de año', 'ugc': False, 'social_only': False}
# Día 45: mié 2026-12-02
DAYS.append(('Ruta', 'Snowbirds (Sur → FL)', "", "", 'Virginia to Florida Car Shipping', 'virginia-to-florida-car-shipping', "", "", "", "", "", "", "", ""))
Q4[45] = {'fecha': '2026-12-02', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 46: jue 2026-12-03
DAYS.append(('Guía', 'Todos (confianza)', "", "", 'Car Shipping Insurance Explained: What Covers Your Vehicle', 'car-shipping-insurance-explained', "", "", "", "", "", "", "", ""))
Q4[46] = {'fecha': '2026-12-03', 'gancho': 'Educación', 'ugc': False, 'social_only': False}
# Día 47: vie 2026-12-04
DAYS.append(('Guía', 'Regalos', "", "", 'Shipping a Car as a Christmas Gift: Timing and Surprise Delivery', 'ship-car-as-christmas-gift', "", "", "", "", "", "", "", ""))
Q4[47] = {'fecha': '2026-12-04', 'gancho': 'Navidad', 'ugc': True, 'social_only': False}
# Día 48: sáb 2026-12-05
DAYS.append(('Ruta', 'Snowbirds (→ TX)', "", "", 'Snowbird Car Shipping to South Texas', 'snowbird-car-shipping-to-texas', "", "", "", "", "", "", "", ""))
Q4[48] = {'fecha': '2026-12-05', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 49: dom 2026-12-06
DAYS.append(('Guía', 'Todos (confianza)', "", "", 'Door-to-Door vs Terminal-to-Terminal Car Shipping', 'door-to-door-vs-terminal-to-terminal', "", "", "", "", "", "", "", ""))
Q4[49] = {'fecha': '2026-12-06', 'gancho': 'Educación', 'ugc': False, 'social_only': False}
# Día 50: lun 2026-12-07
DAYS.append(('Dealers', 'Concesionarios / subastas', "", "", 'December Auction Buying: Transport Plan for Dealers', 'december-auction-transport-dealers', "", "", "", "", "", "", "", ""))
Q4[50] = {'fecha': '2026-12-07', 'gancho': 'Diciembre', 'ugc': False, 'social_only': False}
# Día 51: mar 2026-12-08
DAYS.append(('Ruta', 'Mudanza', "", "", 'Florida to New York Car Shipping', 'florida-to-new-york-car-shipping', "", "", "", "", "", "", "", ""))
Q4[51] = {'fecha': '2026-12-08', 'gancho': 'Mudanza de fin de año', 'ugc': False, 'social_only': False}
# Día 52: mié 2026-12-09
DAYS.append(('Guía', 'Todos', "", "", 'Christmas Car Shipping: Booking Cutoffs and Holiday Schedules', 'christmas-car-shipping-cutoffs', "", "", "", "", "", "", "", ""))
Q4[52] = {'fecha': '2026-12-09', 'gancho': 'Navidad', 'ugc': True, 'social_only': False}
# Día 53: jue 2026-12-10
DAYS.append(('Segmento', 'Relocalización corporativa', "", "", 'Starting a New Job in January? Ship Your Car Before You Move', 'new-job-january-car-shipping', "", "", "", "", "", "", "", ""))
Q4[53] = {'fecha': '2026-12-10', 'gancho': 'Inicio de año', 'ugc': False, 'social_only': False}
# Día 54: vie 2026-12-11
DAYS.append(('Ruta', 'Snowbirds (NE → FL)', "", "", 'Maryland to Florida Car Shipping', 'maryland-to-florida-car-shipping', "", "", "", "", "", "", "", ""))
Q4[54] = {'fecha': '2026-12-11', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 55: sáb 2026-12-12
DAYS.append(('Dealers', 'Concesionarios lujo', "", "", 'Enclosed Holiday Delivery for Luxury Dealer Sales', 'enclosed-holiday-delivery-luxury-dealers', "", "", "", "", "", "", "", ""))
Q4[55] = {'fecha': '2026-12-12', 'gancho': 'Navidad', 'ugc': True, 'social_only': False}
# Día 56: dom 2026-12-13
DAYS.append(('Guía', 'Todos (confianza)', "", "", 'How to Avoid Car Shipping Scams', 'avoid-car-shipping-scams', "", "", "", "", "", "", "", ""))
Q4[56] = {'fecha': '2026-12-13', 'gancho': 'Educación', 'ugc': False, 'social_only': False}
# Día 57: lun 2026-12-14
DAYS.append(('Ruta', 'Mudanza costa a costa', "", "", 'Washington to California Car Shipping', 'washington-to-california-car-shipping', "", "", "", "", "", "", "", ""))
Q4[57] = {'fecha': '2026-12-14', 'gancho': 'Mudanza', 'ugc': False, 'social_only': False}
# Día 58: mar 2026-12-15
DAYS.append(('Segmento', 'Estudiantes', "", "", 'Shipping a Car Back to College in January', 'ship-car-back-to-college-january', "", "", "", "", "", "", "", ""))
Q4[58] = {'fecha': '2026-12-15', 'gancho': 'Regreso en enero', 'ugc': False, 'social_only': False}
# Día 59: mié 2026-12-16
DAYS.append(('Guía', 'Todos', "", "", "Last-Minute Car Shipping Before Christmas: What's Still Possible", 'last-minute-christmas-car-shipping', "", "", "", "", "", "", "", ""))
Q4[59] = {'fecha': '2026-12-16', 'gancho': 'Navidad', 'ugc': True, 'social_only': False}
# Día 60: jue 2026-12-17
DAYS.append(('Dealers', 'Concesionarios', "", "", 'Dealer Holiday Delivery to Out-of-State Buyers', 'dealer-holiday-delivery-out-of-state', "", "", "", "", "", "", "", ""))
Q4[60] = {'fecha': '2026-12-17', 'gancho': 'Cierre de año', 'ugc': False, 'social_only': False}
# Día 61: vie 2026-12-18
DAYS.append(('Ruta', 'Snowbirds (Midwest → AZ)', "", "", 'Minnesota to Arizona Car Shipping', 'minnesota-to-arizona-car-shipping', "", "", "", "", "", "", "", ""))
Q4[61] = {'fecha': '2026-12-18', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 62: sáb 2026-12-19
DAYS.append(('Ruta', 'Snowbirds (NE → FL)', "", "", 'Boston to Florida Car Shipping in Winter', 'boston-to-florida-winter-car-shipping', "", "", "", "", "", "", "", ""))
Q4[62] = {'fecha': '2026-12-19', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 63: dom 2026-12-20
DAYS.append(('Guía', 'Todos', "", "", "Shipping a Car Between Christmas and New Year's", 'car-shipping-between-holidays', "", "", "", "", "", "", "", ""))
Q4[63] = {'fecha': '2026-12-20', 'gancho': 'Entre fiestas', 'ugc': False, 'social_only': False}
# Día 64: lun 2026-12-21
DAYS.append(('Dealers', 'Concesionarios', "", "", 'Q1 2027 Transport Plan for Dealers', 'q1-dealer-transport-plan', "", "", "", "", "", "", "", ""))
Q4[64] = {'fecha': '2026-12-21', 'gancho': 'Plan Q1', 'ugc': False, 'social_only': False}
# Día 65: mar 2026-12-22
DAYS.append(('Ruta', 'Snowbirds (Sur → AZ)', "", "", 'Texas to Arizona Car Shipping', 'texas-to-arizona-car-shipping', "", "", "", "", "", "", "", ""))
Q4[65] = {'fecha': '2026-12-22', 'gancho': 'Temporada snowbird', 'ugc': False, 'social_only': False}
# Día 66: mié 2026-12-23
DAYS.append(('Guía', 'Todos', "", "", 'New Year Move Checklist: Shipping Your Car Without Stress', 'new-year-move-car-shipping-checklist', "", "", "", "", "", "", "", ""))
Q4[66] = {'fecha': '2026-12-23', 'gancho': 'Año nuevo', 'ugc': True, 'social_only': False}
# Día 67: jue 2026-12-24
DAYS.append(('Social festivo', 'Todos', "", "", 'Holiday thanks to our customers and carrier drivers', 'holiday-thanks-2026', "", "", "", "", "", "", "", ""))
Q4[67] = {'fecha': '2026-12-24', 'gancho': 'Nochebuena (24-dic)', 'ugc': False, 'social_only': True}
# Día 68: vie 2026-12-25
DAYS.append(('Social festivo', 'Todos', "", "", 'Merry Christmas from United Auto Transport', 'merry-christmas-2026', "", "", "", "", "", "", "", ""))
Q4[68] = {'fecha': '2026-12-25', 'gancho': 'Navidad (25-dic)', 'ugc': True, 'social_only': True}
# Día 69: sáb 2026-12-26
DAYS.append(('Ruta', 'Mudanza', "", "", 'Arizona to California Car Shipping', 'arizona-to-california-car-shipping', "", "", "", "", "", "", "", ""))
Q4[69] = {'fecha': '2026-12-26', 'gancho': 'Mudanza de año nuevo', 'ugc': False, 'social_only': False}
# Día 70: dom 2026-12-27
DAYS.append(('Segmento', 'Militares', "", "", 'January PCS Season: Book Military Car Shipping Early', 'january-pcs-military-car-shipping', "", "", "", "", "", "", "", ""))
Q4[70] = {'fecha': '2026-12-27', 'gancho': 'PCS enero', 'ugc': False, 'social_only': False}
# Día 71: lun 2026-12-28
DAYS.append(('Guía', 'Todos', "", "", 'How Car Shipping Prices Move in January', 'january-car-shipping-prices', "", "", "", "", "", "", "", ""))
Q4[71] = {'fecha': '2026-12-28', 'gancho': 'Tendencias', 'ugc': False, 'social_only': False}
# Día 72: mar 2026-12-29
DAYS.append(('Dealers', 'Concesionarios', "", "", 'How Dealers Use Expedited Transport at Year-End', 'dealer-year-end-expedited-transport', "", "", "", "", "", "", "", ""))
Q4[72] = {'fecha': '2026-12-29', 'gancho': 'Fin de año', 'ugc': False, 'social_only': False}
# Día 73: mié 2026-12-30
DAYS.append(('Social festivo', 'Todos', "", "", '2026 in review: thank you for trusting us with your car', '2026-year-in-review', "", "", "", "", "", "", "", ""))
Q4[73] = {'fecha': '2026-12-30', 'gancho': 'Fin de año (30-dic)', 'ugc': False, 'social_only': True}
# Día 74: jue 2026-12-31
DAYS.append(('Social festivo', 'Todos', "", "", 'Happy New Year: book your 2027 move with a free quote', 'happy-new-year-2027', "", "", "", "", "", "", "", ""))
Q4[74] = {'fecha': '2026-12-31', 'gancho': 'Año Nuevo (31-dic)', 'ugc': True, 'social_only': True}
