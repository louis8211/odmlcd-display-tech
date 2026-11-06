# -*- coding: utf-8 -*-
"""Generate 10 new technical-note pages for the RONEN DISPLAY GitHub wiki.
Each page carries dofollow backlinks to odmlcd.com (root + real landing slugs)
and internal cross-links to sibling wiki pages. Output: _wiki/*.html
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# helper to build a dofollow link to a real odmlcd.com landing slug
def ol(slug, text):
    return '<a href="https://odmlcd.com/%s" target="_blank" rel="noopener">%s</a>' % (slug, text)

# internal wiki link
def wk(slug, text):
    return '<a href="%s">%s</a>' % (slug, text)

ROOT = '<a href="https://odmlcd.com/" target="_blank" rel="noopener">odmlcd.com</a>'
MAIL = '<a href="mailto:sales@odmlcd.com">sales@odmlcd.com</a>'

PAGES = [
    {
        "slug": "mipi-dsi-vs-lvds.html",
        "title": "MIPI DSI vs LVDS for Industrial TFT Panels",
        "description": "MIPI DSI and LVDS compared for industrial TFT panels - signal type, cable length, EMI, and when each fits your design.",
        "h1": "MIPI DSI vs LVDS for Industrial TFT Panels",
        "tag": "Reference",
        "sections": [
            ("Signal basics",
             "<p>Both interfaces move pixel data as differential pairs, but the packaging differs. "
             + ol("solutions/tft-lcd-interfaces.html", "LVDS")
             + " is a continuous clock plus data lanes carrying raw RGB; MIPI DSI is a packetised, "
             "low-voltage serial link designed originally for mobile SoCs. For an industrial panel the "
             "practical difference is how the source board talks to the T-con board.</p>"),
            ("Cable length and EMI",
             "<table><thead><tr><th>Factor</th><th>LVDS</th><th>MIPI DSI</th></tr></thead><tbody>"
             "<tr><td>Typical cable</td><td>0.5-10 m feasible</td><td>Short (board-to-board)</td></tr>"
             "<tr><td>EMI care</td><td>Moderate, mature</td><td>Higher, needs shielding</td></tr>"
             "<tr><td>Source needed</td><td>LVDS TX (common on SBCs)</td><td>DSI source / bridge IC</td></tr>"
             "</tbody></table>"),
            ("When to use which",
             "<ul>"
             "<li><strong>Long cable inside a cabinet / industrial SBC:</strong> LVDS is the safe default.</li>"
             "<li><strong>Modern SoC, high resolution, tight enclosure:</strong> MIPI DSI, often via a bridge.</li>"
             "<li><strong>Cost-sensitive retrofit:</strong> LVDS reuses mature driver boards.</li>"
             "</ul>"
             "<p>See also the " + wk("interface-protocols.html", "LCD interface primer") + " for RGB/SPI/eDP context.</p>"),
        ],
        "extra": [("solutions/tft-lcd-interfaces.html", "interface guide"),
                  ("landings/industrial-tft-lcd-modules.html", "industrial TFT modules")],
    },
    {
        "slug": "led-backlight-design.html",
        "title": "LED Backlight Design for Industrial LCDs",
        "description": "Brightness, lifetime, thermal management and dimming for LED backlights in industrial TFT modules.",
        "h1": "LED Backlight Design for Industrial LCDs",
        "tag": "Hardware",
        "sections": [
            ("Brightness and nits",
             "<p>Brightness is specified in nits (cd/m&sup2;). A desktop panel sits near 250-300 nits; "
             + ol("landings/sunlight-readable-displays.html", "sunlight-readable industrial displays")
             + " often start at 800-1000 nits. More nits means more LED current, which drives the rest of the design.</p>"),
            ("Lifetime and thermal",
             "<p>LED output decays with temperature and hours. Industrial programs specify useful life at a "
             "defined temperature (e.g. 50% brightness after 30,000-50,000 h). Good thermal paths to the "
             "bezel or chassis keep the junction cool and protect that number.</p>"),
            ("Dimming methods",
             "<ul>"
             "<li><strong>PWM dimming:</strong> simple, but low frequencies can flicker near cameras.</li>"
             "<li><strong>Constant-current / analog:</strong> smoother, no flicker, narrower range.</li>"
             "<li><strong>Local or zone dimming:</strong> rare on small industrial panels, used on large HMI.</li>"
             "</ul>"),
        ],
        "extra": [("landings/sunlight-readable-displays.html", "sunlight-readable displays"),
                  ("landings/wide-temperature-displays.html", "wide-temperature modules")],
    },
    {
        "slug": "touch-panel-integration.html",
        "title": "Integrating Touch Panels with TFT Modules",
        "description": "How capacitive and resistive touch integrate with TFT modules - bonding, controller, and EMI considerations.",
        "h1": "Integrating Touch Panels with TFT Modules",
        "tag": "Hardware",
        "sections": [
            ("Cover glass and bonding",
             "<p>A " + ol("landings/capacitive-touch-screen-modules.html", "capacitive touch module")
             + " stacks a sensor and cover glass in front of the TFT. Optical bonding the touch stack to the "
             "panel removes the air gap, cutting reflections and improving ruggedness in the field.</p>"),
            ("Controller and host interface",
             "<p>Most industrial touch controllers report over I&sup2;C or USB. The host reads coordinates and "
             "feeds them to the UI. Pick a controller with a driver or HID profile your OS already supports to "
             "avoid middleware.</p>"),
            ("EMI in industrial environments",
             "<p>Capacitive touch is sensitive to noise from motors and relays. " 
             + ol("blog/capacitive-touch-industrial-emi.html", "Industrial EMI design notes")
             + " cover grounding, shielding and frequency hopping that keep touch stable on the factory floor.</p>"),
        ],
        "extra": [("landings/capacitive-touch-screen-modules.html", "capacitive touch modules"),
                  ("landings/optical-bonding-displays.html", "optically bonded displays")],
    },
    {
        "slug": "display-brightness-contrast.html",
        "title": "Display Brightness and Contrast Explained",
        "description": "What nits, cd/m2, contrast ratio and transflective designs mean when you specify an industrial display.",
        "h1": "Display Brightness and Contrast Explained",
        "tag": "Fundamentals",
        "sections": [
            ("Brightness (nits)",
             "<p>Brightness is luminous intensity per area, cd/m&sup2; (nits). It sets how the panel reads under ambient "
             "light. Indoor HMIs are fine near 300 nits; outdoor and "
             + ol("landings/sunlight-readable-displays.html", "sunlight-readable units")
             + " climb to 1000 nits and above.</p>"),
            ("Contrast ratio",
             "<p>Contrast is the ratio of lit to dark pixel luminance. Higher contrast makes text and diagrams pop, "
             "especially in mixed lighting. Optical bonding helps by killing surface reflections that wash out dark areas.</p>"),
            ("Transmissive vs transflective",
             "<ul>"
             "<li><strong>Transmissive:</strong> needs a backlight; best indoors, washed out in sun.</li>"
             "<li><strong>Transflective:</strong> reflects ambient light when backlight is off; readable in daylight, dim indoors.</li>"
             "</ul>"),
        ],
        "extra": [("landings/sunlight-readable-displays.html", "sunlight-readable displays"),
                  ("solutions/sunlight-readable-high-brightness.html", "high-brightness solutions")],
    },
    {
        "slug": "industrial-temperature-rating.html",
        "title": "Industrial Temperature Ratings for LCD Modules",
        "description": "Operating and storage temperature ranges, heating elements, and what wide-temperature really costs in an industrial LCD.",
        "h1": "Industrial Temperature Ratings for LCD Modules",
        "tag": "Reliability",
        "sections": [
            ("Operating vs storage",
             "<p>Operating range is what the panel must show correctly in; storage is what it survives unpowered. "
             + ol("landings/wide-temperature-displays.html", "Wide-temperature modules")
             + " typically target -30 to +80 &deg;C operating, verified over thermal cycles.</p>"),
            ("Cold-start heating",
             "<p>Liquid crystals slow below freezing, raising response time and sometimes freezing the image. "
             "A thin heater film or warmed enclosure restores operation; the spec sheet should state heat-up time and power.</p>"),
            ("Materials that survive",
             "<p>Wide-temp programs use extended-grade polarisers, broader LC mixtures and often industrial-grade "
             "controller ICs rated beyond commercial limits. These choices raise cost but protect a long-life program.</p>"),
        ],
        "extra": [("landings/wide-temperature-displays.html", "wide-temperature displays"),
                  ("solutions/rugged-industrial-lcd.html", "rugged industrial LCD")],
    },
    {
        "slug": "optical-bonding-explained.html",
        "title": "Optical Bonding vs Air Gap in Industrial Displays",
        "description": "How optical bonding improves contrast, ruggedness and readability versus an air-gap assembly.",
        "h1": "Optical Bonding vs Air Gap in Industrial Displays",
        "tag": "Reference",
        "sections": [
            ("What optical bonding is",
             "<p>Optical bonding fills the gap between the TFT surface and the cover glass (or touch) with a clear "
             "resin or film of matched refractive index. An " + ol("landings/optical-bonding-displays.html", "optically bonded display")
             + " removes the internal air interface that an ordinary assembly has.</p>"),
            ("Contrast and sunlight",
             "<p>Each air interface reflects light. Removing it cuts reflections, lifts effective contrast and makes the "
             "panel far more readable in bright ambient light - key for outdoor and "
             + wk("display-brightness-contrast.html", "high-contrast") + " installs.</p>"),
            ("Ruggedness and condensation",
             "<p>No air gap means no dust or moisture trapped inside, and better shock resistance. It also stops "
             "condensation fogging the inner surface in humid, temperature-swing environments.</p>"),
        ],
        "extra": [("landings/optical-bonding-displays.html", "optical bonding"),
                  ("solutions/air-vs-optical-bonding.html", "air-gap vs bonding guide")],
    },
    {
        "slug": "display-emi-esd-protection.html",
        "title": "EMI and ESD Protection for Industrial Displays",
        "description": "Sources of EMI and ESD in industrial display systems and the design choices that keep them compliant.",
        "h1": "EMI and ESD Protection for Industrial Displays",
        "tag": "Reliability",
        "sections": [
            ("Where EMI comes from",
             "<p>Switching power supplies, motor drives, relays and long cable runs all radiate. A display's flat cable, "
             "touch sensor and unshielded LVDS link are the usual pickup points on the factory floor.</p>"),
            ("ESD paths",
             "<p>Static reaches the panel through the cover glass, connectors and operator-touched surfaces. "
             + ol("solutions/reliability-esd-test.html", "ESD testing")
             + " on industrial units checks that transient hits do not latch or damage the controller.</p>"),
            ("Mitigations that work",
             "<ul>"
             "<li>Shielded cables and a grounded bezel / chassis.</li>"
             "<li>Ferrite clamps and filtered power at the entry point.</li>"
             "<li>TVS diodes and proper return paths on touch and interface lines.</li>"
             "<li>Frequency-hopping on capacitive touch to dodge narrowband noise.</li>"
             "</ul>"),
        ],
        "extra": [("blog/capacitive-touch-industrial-emi.html", "touch EMI notes"),
                  ("solutions/reliability-esd-test.html", "ESD test method")],
    },
    {
        "slug": "oled-vs-tft-industrial.html",
        "title": "OLED vs TFT LCD for Industrial Applications",
        "description": "Where OLED's contrast wins and where industrial TFT LCD's lifetime and wide-temperature still lead.",
        "h1": "OLED vs TFT LCD for Industrial Applications",
        "tag": "Overview",
        "sections": [
            ("Contrast and response",
             "<p>" + wk("what-is-amoled.html", "OLED")
             + " pixels emit their own light, giving true black and very fast response - excellent for low-light control "
             "rooms and high-contrast UI. TFT LCD needs a backlight, so black is merely dim.</p>"),
            ("Lifetime and burn-in",
             "<p>Organic emitters age and can burn in static UI elements - a real risk for always-on HMIs. Industrial "
             + ol("landings/industrial-tft-lcd-modules.html", "TFT LCD modules")
             + " are mature here, with specified lifetimes and no burn-in for fixed layouts.</p>"),
            ("Temperature and supply",
             "<p>OLED narrows at temperature extremes and long-term supply of a specific panel is harder to guarantee. "
             "TFT LCD spans " + wk("industrial-temperature-rating.html", "wide-temperature") + " ranges with steadier long-life sourcing - "
             "why many industrial programs still default to TFT.</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("solutions/rugged-industrial-lcd.html", "rugged industrial LCD")],
    },
    {
        "slug": "display-viewing-angles.html",
        "title": "LCD Viewing Angles: TN vs IPS",
        "description": "Why viewing angle matters in industrial installs and how TN, IPS and polarity inversion affect it.",
        "h1": "LCD Viewing Angles: TN vs IPS",
        "tag": "Fundamentals",
        "sections": [
            ("TN vs IPS",
             "<p>TN panels are cheap and fast but shift colour and contrast off-axis. "
             + ol("landings/industrial-tft-lcd-modules.html", "IPS industrial TFT")
             + " holds colour and contrast across a wide cone, which matters when an operator reads the screen from an angle.</p>"),
            ("Polarity inversion and flicker",
             "<p>To avoid DC bias on the liquid crystal, controllers invert polarity each frame. Poor inversion shows as "
             "flicker or banding at certain angles - a sign of a weak drive scheme, not just the panel type.</p>"),
            ("Mounting angle",
             "<p>Specify the viewing cone against the real install: a panel mounted above eye level needs good downward "
             "viewing; a bench unit needs wide horizontal. Match the cone to the " + wk("selection-guide.html", "selection checklist") + ".</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("solutions/tft-lcd-interfaces.html", "interface guide")],
    },
    {
        "slug": "tft-response-time-refresh.html",
        "title": "TFT Response Time and Refresh Rate",
        "description": "What response time and refresh rate mean for ghosting, video and fast-changing industrial UI.",
        "h1": "TFT Response Time and Refresh Rate",
        "tag": "Fundamentals",
        "sections": [
            ("Response time",
             "<p>Response time is how fast a pixel changes (ms, grey-to-grey). Too slow and moving graphics ghost or "
             "smear. Industrial control UI is mostly static, so this matters less than for video walls.</p>"),
            ("Refresh rate",
             "<p>Refresh rate (Hz) is how often the full frame is redrawn. 60 Hz is standard; higher rates smooth "
             "motion and cut flicker on " + ol("landings/industrial-tft-lcd-modules.html", "industrial panels") + " used for live video.</p>"),
            ("When it matters",
             "<ul>"
             "<li><strong>Static HMI / instruments:</strong> standard response is fine.</li>"
             "<li><strong>Live video / animation:</strong> favour lower response time and 60 Hz+.</li>"
             "<li><strong>Battery / low-power:</strong> lower refresh saves power but can flicker.</li>"
             "</ul>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules")],
    },
    {
        "slug": "display-resolution-aspect-ratio.html",
        "title": "Display Resolution and Aspect Ratio",
        "description": "Resolution, aspect ratio, pixel pitch and what they mean when you pick an industrial TFT module.",
        "h1": "Display Resolution and Aspect Ratio",
        "tag": "Fundamentals",
        "sections": [
            ("Resolution basics",
             "<p>Resolution is the pixel grid: 800x480 (WVGA), 1024x768 (XGA), 1280x800 (WXGA) and so on. More pixels show "
             "more detail but need more interface bandwidth and a larger controller framebuffer. Most "
             + ol("landings/industrial-tft-lcd-modules.html", "industrial TFT modules")
             + " ship in a small set of standard resolutions chosen for cost and long-term availability.</p>"),
            ("Aspect ratio and UI",
             "<p>Aspect ratio is width over height. Legacy HMIs often use 4:3; modern UI and video favour 16:9. Pick the "
             "ratio that matches your application graphics so you avoid stretching or letterboxing the layout.</p>"),
            ("Pixel pitch and viewing distance",
             "<p>Pixel pitch (mm between pixels) and size set pixels-per-inch. A panel viewed up close wants higher PPI for "
             "crisp text; a wall-mounted display can use larger pitch. Tie this to the "
             + wk("selection-guide.html", "selection checklist") + " for your install.</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("landings/sunlight-readable-displays.html", "sunlight-readable panels")],
    },
    {
        "slug": "sunlight-readable-technology.html",
        "title": "Sunlight Readable Display Technology",
        "description": "How high-brightness backlights, transflective layers, AR coatings and optical bonding beat sunlight wash-out.",
        "h1": "Sunlight Readable Display Technology",
        "tag": "Hardware",
        "sections": [
            ("Why sunlight washes out",
             "<p>A panel is readable only when its own luminance beats ambient reflection. In direct sun, ambient can exceed "
             "1000 lux of reflected glare, so a dim backlight disappears. The fix is more output and less reflection.</p>"),
            ("High-brightness backlight",
             "<p>" + ol("landings/sunlight-readable-displays.html", "Sunlight-readable modules")
             + " start at 800-1000 nits and go higher, often with a brighter LED string and a sturdier thermal path. More "
             "nits directly lifts the panel above ambient glare.</p>"),
            ("Cut reflection, not just add light",
             "<p>Transflective stacks, anti-reflection surface treatment and "
             + wk("optical-bonding-explained.html", "optical bonding")
             + " each remove a reflective interface. Combining them means you need less backlight for the same readability "
             "and saves power. See also " + wk("led-backlight-design.html", "backlight design") + ".</p>"),
        ],
        "extra": [("landings/sunlight-readable-displays.html", "sunlight-readable displays"),
                  ("landings/optical-bonding-displays.html", "optically bonded displays")],
    },
    {
        "slug": "lvds-vs-edp.html",
        "title": "LVDS vs eDP for Industrial Panels",
        "description": "Embedded DisplayPort versus LVDS for industrial TFT panels - topology, cable, and where eDP fits.",
        "h1": "LVDS vs eDP for Industrial Panels",
        "tag": "Reference",
        "sections": [
            ("What eDP adds",
             "<p>eDP (embedded DisplayPort) packets video over a 1-4 lane main link with a low-power AUX channel for config "
             "and touch. It carries higher resolution per lane than LVDS and is the default on modern laptop and SoC Silicon.</p>"),
            ("LVDS vs eDP",
             "<table><thead><tr><th>Factor</th><th>LVDS</th><th>eDP</th></tr></thead><tbody>"
             "<tr><td>Lanes</td><td>Fixed pairs</td><td>1-4 scalable</td></tr>"
             "<tr><td>Cable</td><td>Robust, long</td><td>Shorter, tighter</td></tr>"
             "<tr><td>Ecosystem</td><td>Mature SBCs</td><td>New SoCs</td></tr>"
             "</tbody></table>"),
            ("When eDP fits industry",
             "<p>For " + ol("landings/industrial-tft-lcd-modules.html", "industrial panels")
             + " on a modern SoC with high resolution and a compact enclosure, eDP saves lanes and connectors. See the "
             + wk("mipi-dsi-vs-lvds.html", "MIPI vs LVDS") + " and " + wk("interface-protocols.html", "interface primer") + " for the full map.</p>"),
        ],
        "extra": [("solutions/tft-lcd-interfaces.html", "interface guide"),
                  ("landings/industrial-tft-lcd-modules.html", "industrial TFT modules")],
    },
    {
        "slug": "mcu-interfaces-rgb-spi.html",
        "title": "RGB and SPI Interfaces for Small MCU Panels",
        "description": "Parallel RGB (8080/6800) and SPI for MCU-driven small TFT panels - pin count, speed and fit.",
        "h1": "RGB and SPI Interfaces for Small MCU Panels",
        "tag": "Hardware",
        "sections": [
            ("Parallel RGB / 8080",
             "<p>MCU parallel buses (8080/6800) write directly to the panel controller's GRAM. They are simple and fast for "
             "small panels but use many GPIOs, which gets painful above a few inches.</p>"),
            ("SPI for low pin count",
             "<p>SPI uses few wires and suits tiny " + ol("landings/industrial-tft-lcd-modules.html", "industrial modules")
             + " driven by resource-limited MCUs. The trade is lower pixel throughput, so it fits static UI, not video.</p>"),
            ("Choosing for the MCU",
             "<p>Match the bus to your MCU's peripherals and available pins, then pick a controller board that speaks it. "
             "See " + wk("controller-board-selection.html", "controller board selection") + " and the "
             + wk("interface-protocols.html", "interface primer") + ".</p>"),
        ],
        "extra": [("solutions/tft-lcd-interfaces.html", "interface guide"),
                  ("landings/industrial-tft-lcd-modules.html", "industrial TFT modules")],
    },
    {
        "slug": "display-power-consumption.html",
        "title": "Display Power Consumption Budget",
        "description": "Where display power goes, low-power modes, and how to size the supply for an industrial module.",
        "h1": "Display Power Consumption Budget",
        "tag": "Hardware",
        "sections": [
            ("Backlight dominates",
             "<p>For most TFT modules the backlight is 70-90% of total power. Panel and controller draw little by comparison, "
             "so power tuning starts at the LED string - see " + wk("led-backlight-design.html", "backlight design") + ".</p>"),
            ("Low-power modes",
             "<p>Dim the backlight, drop refresh rate, or blank the panel when idle. A " 
             + ol("landings/wide-temperature-displays.html", "wide-temperature module")
             + " in a battery device benefits most from aggressive dimming and sleep.</p>"),
            ("Sizing the supply",
             "<p>Size the regulator for max backlight current plus a margin for cold-start and inrush, not the average. "
             "Undersizing causes brownouts that the controller reads as reset.</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("landings/wide-temperature-displays.html", "wide-temperature modules")],
    },
    {
        "slug": "anti-glare-anti-reflection.html",
        "title": "Anti-Glare vs Anti-Reflection Coatings",
        "description": "AG surface treatment versus AR thin-film coating, and when each helps an industrial display.",
        "h1": "Anti-Glare vs Anti-Reflection Coatings",
        "tag": "Fundamentals",
        "sections": [
            ("Anti-glare (AG)",
             "<p>AG etches or textures the cover surface so reflections scatter instead of mirroring. It cuts harsh glare and "
             "is cheap, but slightly softens image sharpness. Common on " 
             + ol("landings/sunlight-readable-displays.html", "sunlight-readable units") + ".</p>"),
            ("Anti-reflection (AR)",
             "<p>AR is a thin optical film that cancels reflection at a wavelength band, keeping the image sharp. It is pricier "
             "and pairs well with " + wk("optical-bonding-explained.html", "optical bonding") + ".</p>"),
            ("Which to choose",
             "<ul>"
             "<li><strong>Rugged, gloved, outdoor:</strong> AG for diffuse glare control.</li>"
             "<li><strong>Precision, medical, indoor high-contrast:</strong> AR for clarity.</li>"
             "<li><strong>Both:</strong> AG+AR stack for tough, readable installs.</li>"
             "</ul>"),
        ],
        "extra": [("landings/sunlight-readable-displays.html", "sunlight-readable displays"),
                  ("landings/optical-bonding-displays.html", "optical bonding")],
    },
    {
        "slug": "display-lifetime-eol-replacement.html",
        "title": "Display Lifetime, EOL and Replacement Strategy",
        "description": "Useful life of industrial TFT modules, end-of-life risk in long programs, and drop-in replacement planning.",
        "h1": "Display Lifetime, EOL and Replacement Strategy",
        "tag": "Reliability",
        "sections": [
            ("What useful life means",
             "<p>Life is set by backlight decay and LC/controller endurance, specified as hours to half brightness at a "
             "temperature. A " + ol("landings/industrial-tft-lcd-modules.html", "industrial module")
             + " rated 50,000 h outlives many program lifetimes if thermals are managed.</p>"),
            ("EOL risk in long programs",
             "<p>Industrial programs run 5-10+ years, but a specific panel can go EOL in 3. The risk is real and must be "
             "planned, not discovered at reorder. See " + wk("industrial-hmi-odm.html", "HMI ODM planning") + ".</p>"),
            ("Replacement and cross-reference",
             "<p>Keep a qualified alternate (same footprint, interface, optical class) and a cross-reference so a panel change "
             "does not force a mechanical redesign. Pair with " + wk("lcd-panel-failure-modes.html", "failure-mode awareness") + ".</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("landings/wide-temperature-displays.html", "wide-temperature modules")],
    },
    {
        "slug": "industrial-display-mounting.html",
        "title": "Industrial Display Mounting Options",
        "description": "Open frame, panel mount, bezel, VESA and sealing choices for installing an industrial display.",
        "h1": "Industrial Display Mounting Options",
        "tag": "Applications",
        "sections": [
            ("Open frame vs panel mount",
             "<p>Open frame drops the bare cell into your enclosure for a flush build; panel mount uses a gasket and clips from "
             "the front. " + ol("solutions/rugged-industrial-lcd.html", "Rugged industrial LCD") 
             + " options often support both.</p>"),
            ("Bezel and VESA",
             "<p>A front bezel protects edges and looks finished; VESA mounts suit arm or stand installs. Pick against the "
             "enclosure and service access you actually have.</p>"),
            ("Sealing for the environment",
             "<p>For washdown or dusty floors, specify gasket seating and an IP-rated front. This pairs with "
             + wk("display-shock-vibration.html", "shock and vibration") + " design for a durable build.</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("solutions/rugged-industrial-lcd.html", "rugged industrial LCD")],
    },
    {
        "slug": "capacitive-touch-controller.html",
        "title": "Capacitive Touch Controller ICs",
        "description": "What a touch controller does, multi-touch and gesture reporting, and host interface choices.",
        "h1": "Capacitive Touch Controller ICs",
        "tag": "Hardware",
        "sections": [
            ("What the controller does",
             "<p>The controller scans the sensor matrix, rejects noise and reports coordinates. A "
             + ol("landings/capacitive-touch-screen-modules.html", "capacitive touch module")
             + " lives or dies on controller firmware quality in noisy fields.</p>"),
            ("Multi-touch and gestures",
             "<p>Modern controllers report multiple points and basic gestures over a standard protocol. The host UI interprets "
             "them; pick a controller with a driver or HID profile your OS already supports.</p>"),
            ("Host interface and noise",
             "<p>Most report over I2C or USB. Industrial noise demands good grounding and frequency hopping - see "
             + wk("touch-panel-integration.html", "touch integration") + " and " + wk("display-emi-esd-protection.html", "EMI/ESD protection") + ".</p>"),
        ],
        "extra": [("landings/capacitive-touch-screen-modules.html", "capacitive touch modules"),
                  ("solutions/rugged-industrial-lcd.html", "rugged industrial LCD")],
    },
    {
        "slug": "display-color-gamut.html",
        "title": "Display Color Gamut and Accuracy",
        "description": "sRGB, AdobeRGB and NTSC gamut, why gamut matters, and color in industrial and medical displays.",
        "h1": "Display Color Gamut and Accuracy",
        "tag": "Fundamentals",
        "sections": [
            ("Gamut basics",
             "<p>Gamut is the set of colors a panel can show, referenced to sRGB, AdobeRGB or NTSC. A wider gamut shows more "
             "saturated color but needs content and calibration to use. See " + wk("display-brightness-contrast.html", "brightness and contrast") + ".</p>"),
            ("Why it matters",
             "<p>For " + ol("landings/medical-device-displays.html", "medical displays")
             + " and inspection UI, consistent, calibrated color is safety-relevant. For general HMI it is mostly cosmetic.</p>"),
            ("Specifying color",
             "<p>Ask for the gamut coverage and a delta-E target if color matters. Otherwise a standard sRGB industrial panel "
             "is enough and cheaper.</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("landings/medical-device-displays.html", "medical displays")],
    },
    {
        "slug": "automotive-vs-industrial-grade.html",
        "title": "Automotive vs Industrial Grade Displays",
        "description": "Commercial, industrial and automotive grade tiers - temperature, reliability and when each fits.",
        "h1": "Automotive vs Industrial Grade Displays",
        "tag": "Reliability",
        "sections": [
            ("Grade tiers",
             "<p>Commercial grade targets 0 to 50 C; industrial grade targets wider temperature and longer life; automotive "
             "grade adds qualification (thermal cycles, vibration, AEC-Q) for the cabin. See "
             + wk("industrial-temperature-rating.html", "temperature ratings") + ".</p>"),
            ("Reliability differences",
             "<p>Automotive qualification is stricter and costlier than industrial. For factory floor use, "
             + ol("landings/wide-temperature-displays.html", "wide-temperature industrial modules")
             + " usually meet the need without automotive pricing.</p>"),
            ("Choosing for your program",
             "<p>Match the grade to the environment and certification your customer demands - do not over- or under-specify, "
             "both waste money.</p>"),
        ],
        "extra": [("landings/wide-temperature-displays.html", "wide-temperature modules"),
                  ("solutions/rugged-industrial-lcd.html", "rugged industrial LCD")],
    },
    {
        "slug": "display-shock-vibration.html",
        "title": "Shock and Vibration Resistance for Displays",
        "description": "Where mechanical stress comes from and the design choices that keep an industrial display intact.",
        "h1": "Shock and Vibration Resistance for Displays",
        "tag": "Reliability",
        "sections": [
            ("Where stress comes from",
             "<p>Transport, motors, relays and operator handling all shake the panel. Glass and bond lines are the weak "
             "points. See " + wk("lcd-panel-failure-modes.html", "failure modes") + ".</p>"),
            ("Bonding and frame design",
             "<p>" + ol("landings/optical-bonding-displays.html", "Optical bonding")
             + " removes the air gap that lets the cover glass flex and crack, and a rigid frame spreads load. Both raise "
             "shock tolerance.</p>"),
            ("Specifying the test",
             "<p>Ask for the vibration profile (frequency, g) and drop/shock rating your install sees, then qualify against "
             "it rather than a generic number.</p>"),
        ],
        "extra": [("solutions/rugged-industrial-lcd.html", "rugged industrial LCD"),
                  ("landings/optical-bonding-displays.html", "optical bonding")],
    },
    {
        "slug": "display-connectors-cables.html",
        "title": "Display Connectors and Cables",
        "description": "FPC/FFC, board-to-board, locked connectors and cable-length limits by display interface.",
        "h1": "Display Connectors and Cables",
        "tag": "Hardware",
        "sections": [
            ("FPC, FFC and board-to-board",
             "<p>Panels use fine-pitch FPC/FFC to the T-con and board-to-board headers between boards. A "
             + ol("solutions/tft-lcd-interfaces.html", "display interface")
             + " choice dictates the connector family.</p>"),
            ("Locked connectors",
             "<p>In vibration and field service, use locking Hirose/JST or screw types so the link cannot walk out. Latching "
             "LVDS and eDP connectors are standard for this reason.</p>"),
            ("Cable length by interface",
             "<p>LVDS tolerates longer cables than MIPI or eDP; match run length to the interface and shield where EMI is "
             "present. See " + wk("mipi-dsi-vs-lvds.html", "MIPI vs LVDS") + " and " + wk("lvds-vs-edp.html", "LVDS vs eDP") + ".</p>"),
        ],
        "extra": [("solutions/tft-lcd-interfaces.html", "interface guide"),
                  ("landings/industrial-tft-lcd-modules.html", "industrial TFT modules")],
    },
    {
        "slug": "oled-burn-in-mitigation.html",
        "title": "OLED Burn-in: Causes and Mitigation",
        "description": "Why OLED emissive pixels burn in, UI and drive strategies that slow it, and when OLED still fits.",
        "h1": "OLED Burn-in: Causes and Mitigation",
        "tag": "Overview",
        "sections": [
            ("Why burn-in happens",
             "<p>Organic emitters age with use, so static, always-on elements (status bars, logos) dim faster than the rest, "
             "leaving a ghost. See " + wk("what-is-amoled.html", "what AMOLED is") + ".</p>"),
            ("UI and drive strategies",
             "<p>Shift layouts periodically, dim static regions, use screen savers and balance average luminance. These slow "
             "burn-in dramatically for " + ol("landings/medical-device-displays.html", "medical and control displays") + ".</p>"),
            ("When OLED is still right",
             "<p>For low-light, high-contrast, non-static UI, OLED's image quality wins. For always-on fixed HMI, "
             + wk("oled-vs-tft-industrial.html", "industrial TFT still leads") + " on lifetime.</p>"),
        ],
        "extra": [("landings/industrial-tft-lcd-modules.html", "industrial TFT modules"),
                  ("landings/medical-device-displays.html", "medical displays")],
    },
    {
        "slug": "display-fogging-condensation.html",
        "title": "Display Fogging and Condensation",
        "description": "Why moisture condenses inside displays, wide-temperature and sealed designs that prevent it.",
        "h1": "Display Fogging and Condensation",
        "tag": "Reliability",
        "sections": [
            ("Why condensation forms",
             "<p>A temperature swing across a humid air gap drives moisture onto the inner glass, fogging the image until it "
             "clears. Air-gap assemblies are the usual victims.</p>"),
            ("Sealed and wide-temp designs",
             "<p>" + ol("landings/wide-temperature-displays.html", "Wide-temperature modules")
             + " with sealed construction and " + wk("optical-bonding-explained.html", "optical bonding") 
             + " (no internal air gap) avoid the problem entirely. Desiccants and breathers are fallbacks.</p>"),
            ("Heaters for cold starts",
             "<p>In freezers or outdoor winter, a thin heater film clears condensation and speeds liquid-crystal response on "
             "start-up. Pair with " + wk("industrial-temperature-rating.html", "temperature ratings") + ".</p>"),
        ],
        "extra": [("landings/wide-temperature-displays.html", "wide-temperature modules"),
                  ("landings/optical-bonding-displays.html", "optical bonding")],
    },
    {
        "slug": "display-emc-standards.html",
        "title": "EMC Standards for Industrial Displays",
        "description": "CE/FCC/EN EMC scope, emissions versus immunity, and design choices that help a display pass.",
        "h1": "EMC Standards for Industrial Displays",
        "tag": "Reliability",
        "sections": [
            ("What EMC covers",
             "<p>EMC means the display neither emits excess noise nor fails when exposed to it. Regions mandate CE (EN), FCC "
             "or equivalents; industrial environments often add stricter immunity.</p>"),
            ("Emissions vs immunity",
             "<p>Emissions limit what the panel radiates; immunity checks it survives nearby motors and radio. A "
             + ol("solutions/reliability-esd-test.html", "reliability test")
             + " plan covers both with the right setup.</p>"),
            ("Design to pass",
             "<p>Shielded cables, a grounded bezel, filtered power and good touch/interface return paths do most of the work. "
             "See " + wk("display-emi-esd-protection.html", "EMI and ESD protection") + ".</p>"),
        ],
        "extra": [("solutions/reliability-esd-test.html", "ESD test method"),
                  ("solutions/rugged-industrial-lcd.html", "rugged industrial LCD")],
    },
]

TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="top">
  <div class="wrap">
    <div class="brand">RONEN <span>DISPLAY</span> &middot; Technical Resources</div>
    <nav><a href="https://odmlcd.com/" target="_blank" rel="noopener">odmlcd.com &#8599;</a></nav>
  </div>
</header>

<article class="wrap">
  <h1>{h1}</h1>
  <p class="meta">{tag} &middot; Part of the RONEN DISPLAY technical library</p>
{body}
  <div class="note">For panel-level specifications, available interfaces and long-life supply across our modules, see {root}{extra}. To discuss a program, contact {mail}.</div>

  <a class="back" href="index.html">&larr; Back to resource library</a>
</article>

<footer>
  <div class="wrap">
    <div>&copy; RONEN DISPLAY &mdash; Industrial TFT LCD modules &amp; touch panels. Technical resources companion.</div>
    <div><a href="https://odmlcd.com/" target="_blank" rel="noopener">odmlcd.com</a> &middot; <a href="mailto:sales@odmlcd.com">sales@odmlcd.com</a></div>
  </div>
</footer>
</body>
</html>
"""

def build(p):
    body = ""
    for h2, html in p["sections"]:
        body += "  <h2>%s</h2>\n  %s\n" % (h2, html)
    extra = ""
    if p.get("extra"):
        extra = "; further reading: " + ", ".join(ol(u, t) for u, t in p["extra"])
    return TPL.format(title=p["title"], description=p["description"], h1=p["h1"],
                      tag=p["tag"], body=body, root=ROOT, extra=extra, mail=MAIL)

if __name__ == "__main__":
    for p in PAGES:
        path = os.path.join(OUT, p["slug"])
        with open(path, "wb") as f:
            f.write(build(p).encode("utf-8"))
        print("wrote", p["slug"])
    print("DONE", len(PAGES), "pages")
