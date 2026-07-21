/* Self-hosted Cytoscape bundle entry.
 *
 * Bundled by Hugo's js.Build (esbuild) into a single fingerprinted,
 * same-origin ES module. main.js imports this lazily (dynamic import,
 * only once the graph scrolls into view) instead of pulling Cytoscape +
 * fcose from a third-party CDN at runtime. Removing the CDN dependency
 * fixes cold-load latency and the pa11y navigation timeout, and keeps
 * everything on the site's own origin (no third-party request, GDPR-safe).
 */
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";

cytoscape.use(fcose);

export default cytoscape;
