# src/

Zero-dependency JS client wrapping the jsDelivr-hosted JSON. Not required —
you can always just `fetch()` the JSON directly (see the root README) — but
handy if you want the convenience functions or plan to publish this as an
npm package.

To publish it yourself:

1. Update `package.json` with your real GitHub username/repo URL.
2. `npm login`
3. `npm publish`

Then consumers can do `npm install persian-quotes` instead of copying the
file.
