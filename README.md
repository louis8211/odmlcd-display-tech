# RONEN DISPLAY — Technical Resources (GitHub Pages)

Static technical library for engineers specifying industrial TFT LCD modules,
touch panels and HMI displays. Served via GitHub Pages at:

**https://louis8211.github.io/odmlcd-site/**

This is a companion site to the main catalogue at **https://odmlcd.com/**.
All pages link back to odmlcd.com. Mirrored articles carry a `rel="canonical"`
pointer to the original on odmlcd.com.

## Content
- Fundamentals: how an LCD works, what is AMOLED, kinds of displays
- Hardware: controller board selection, LCD interface primer
- Reliability: LCD panel failure modes
- Applications: industrial HMI display ODM
- Reference: reading an LCD datasheet, display selection checklist

## Notes
- Plain static HTML + `style.css`, no build step (`.nojekyll` present).
- Outbound links to odmlcd.com are intentional dofollow references.
- This branch (`gh-pages`) is independent of the website source (`main`);
  it does not affect the Cloudflare deployment of odmlcd.com.
