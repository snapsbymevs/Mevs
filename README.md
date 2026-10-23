# MEVS Photography Portfolio

## Preview
Open `index.html` in a browser. Until the first successful sync, it displays **illustrative placeholders**, not your photographs. Use the Theme button to toggle light/dark.

## Publish free with GitHub Pages
1. Create a **public** GitHub repository called `mevs-portfolio`.
2. Upload the contents of this folder (including `.github/workflows/sync.yml`) to the repository root.
3. In repository **Settings → Pages**, choose **Deploy from a branch**, branch **main**, folder **/(root)**, and Save.
4. Your site will appear at `https://YOUR-GITHUB-USERNAME.github.io/mevs-portfolio/` after deployment.
5. In **Actions**, run **Sync Pixelfed photos** manually. If it succeeds, `photos.json` is created and your actual public photographs appear. Thereafter it runs about every six hours (GitHub schedule may be delayed).

## If the sync fails
Pixelfed's documentation lists the lookup and statuses endpoints, but access can vary by instance and deployment. If the workflow reports 401/403, you may need a Pixelfed personal access token with **read** scope. Create one only through your own account's authorized developer/application interface, and store it in GitHub **Settings → Secrets and variables → Actions** as `PIXELFED_TOKEN`. Never commit a token or password to the repository. If your server does not expose these endpoints to your token, this integration needs an alternate supported feed or server-side authorization approach.

## Notes
- Only public, non-sensitive image posts are included; up to ~400 recent posts are checked.
- Each image in a multi-image post is shown individually.
- The original media is linked from Pixelfed, not reuploaded; availability and cross-site image policies are controlled by Pixelfed.
- Posts remain linked to their original Pixelfed URLs.
- The gallery shows most recent posts first. To reverse, edit `sync.py` before writing JSON.
- Test live image loading after publishing: some Pixelfed hosts may restrict hotlinking.
