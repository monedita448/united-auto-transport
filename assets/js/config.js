/* =========================================================
   UNITED AUTO TRANSPORT — SINGLE SOURCE OF TRUTH
   Edit phone number, hours, and tracking IDs here ONLY.
   Every page reads from this file, so a change here updates
   the whole site — no need to hunt through individual HTML files.

   NOTE ON CALLRAIL: in production, CallRail's own snippet (added
   where marked in main.js) handles Dynamic Number Insertion —
   it will swap the number shown per visitor source automatically.
   The values below are the fallback/default number shown before
   CallRail's script loads, and what's used for the office-hours
   logic below.
   ========================================================= */

window.UAT_CONFIG = {
  brandName: "United Auto Transport",

  phoneDisplay: "(972) 833-2614",
  phoneTel: "+19728332614",

  // Office hours are real in THIS timezone — this is where the closer
  // actually sits. Do not change this to "fix" hours for visitors in
  // other timezones; the site converts the DISPLAY only, see main.js.
  officeTimeZone: "America/Chicago",
  hoursStart: 7,   // 7am Central
  hoursEnd: 20,    // 8pm Central
  daysOpen: [1, 2, 3, 4, 5, 6], // Mon-Sat (0 = Sunday, closed)

  // Placeholder — replace with the real CallRail company script ID if
  // call tracking is ever added later. Not required for launch; see
  // leadWebhookUrl below for the free path this site actually uses.
  callRailScriptId: "PLACEHOLDER_CALLRAIL_SCRIPT_ID",

  // Free lead delivery: a Google Apps Script Web App URL (Sheet + email
  // notification, no third-party service, no submission cap). See
  // LEAD_NOTIFIER_SETUP.md for the five-minute setup. Both the callback
  // form and the quote calculator POST here — leave the placeholder in
  // place and lead data just logs to the console instead of failing.
  leadWebhookUrl: "https://script.google.com/macros/s/AKfycbz9dZlDmSwUfwED3M8tb8wH2bl9UtwtVUePCRixpAZpCXqXH-OEFz6f51Pf4OLuhMxX/exec"
};
