This is the master technical specification for the **Ken-Morel System Interface** portfolio. This document consolidates your technical identity, your specific projects, your aesthetic preferences, and the architectural decisions we’ve made.

---

## 1. The Core Identity & "System" Data

This information forms the "Metadata" of the site, used in the `neofetch` and "Bio" sections.

* **User:** `kenmorel`
* **Role:** Systems Architect / Tooling Engineer / J-Tech Founder.
* **Uptime:** 17 Years (Born October 2008).
* **Location:** Yaoundé, Cameroon (JHIS).
* **OS/Environment:** Arch Linux, Hyprland (Wayland), Fish Shell, Ghostty Terminal, Helix Editor.
* **Philosophy:** "Strictly Orthogonal" (No border-radius, 0px blur, pixel-perfect alignment).
* **Soundtrack:** Richard Bona, Creepy Nuts (via Spotify API).

---

## 2. Global Layout: The Desktop Environment

The site behaves like a Tiling Window Manager (TWM) environment built in **SvelteKit**.

### The Waybar (Top Horizontal Bar)

* **Modules (Left):** Workspace indicators `[1] [2] [3] [4]`.
* **Modules (Center):** Current Process/Window Title (e.g., `helix ~/projects/gama.h`).
* **Modules (Right):**
* Spotify "Now Playing" (Marquee text style).
* System Stats (Fake or real browser-thread metrics for CPU/RAM).
* Clock (WAT - West Africa Time).



### The Workspace (Central Container)

* **Visuals:** A single "window" representing a Ghostty instance with 10px "Hyprland gaps" around it.
* **Border:** 1px solid, sharp corners, hex colors from your personal config (Gruvbox/Catppuccin).

---

## 3. Workspace Mapping (The Pages)

### Workspace [1]: The Login / Fetch

* **Command:** `whoami && neofetch`
* **Left Side:** ASCII art of your profile or a pixelated "Kitty Image Protocol" render.
* **Right Side:** System info (Uptime: 17y, Host: JHIS, Shell: fish, Editor: helix).
* **Below:** A "Live Log" of your recent activity (e.g., "Logged in at JHIS," "Developing J-Tech").

### Workspace [2]: The Projects (File Manager Style)

* **Interface:** A TUI-style split (like **Yazi** or **Ranger**).
* **The List (Left):**
* `gama/`: C Game Toolchain (V/Zig/WASM). Stack-first, heap-less philosophy.
* `alat/`: Cross-device service sharing (Go core transitioning to Rust).
* `efus.jl/`: Reactive Julia UI component language (Macro expansion).
* `rrr/`: Remote REPL Runner (Rust).
* `arb-util/`: Parallelized i18n tool (Rust/Fish/Llama.cpp).


* **The Preview (Right):** Renders the project's README and technical architecture diagrams.

### Workspace [3]: The Technical Stack (Process Monitor)

* **Interface:** Styled like `btop` or `htop`.
* **Tables/Graphs:**
* **Memory Usage:** Your proficiency in Rust, C, Go, Julia, V.
* **Running Tasks:** Your experience with TIC Summit 2025 (Record Breakers), Hack Club Daydream (Organizer).
* **Network:** Social links (GitHub: ken-morel, LinkedIn: engon-morel, Discord).



### Workspace [4]: The AI Shell (REPL)

* **Interface:** A raw terminal prompt for the **Ollama Proxy**.
* **Command:** `ask-ai --query "..."`
* **Function:** Communicates with your local Llama models via Tailscale/Cloudflare Tunnel.
* **Feedback:** Streams text token-by-token with a CLI cursor.

---

## 4. Interaction & UX (The Helix Engine)

The site is navigated primarily via keyboard to satisfy "Power User" expectations.

* **The Leader Key:** `Space`
* **Navigation (Helix Style):**
* `gn`: Go to next Workspace.
* `gp`: Go to previous Workspace.
* `j` / `k`: Scroll the current buffer/terminal output.


* **Command Palette:** `Space + f` opens a fuzzy finder to jump directly to any project or section.
* **Modes:**
* `NORMAL`: Keybindings are active.
* `INSERT`: AI Shell is active (keyboard input goes to the prompt).



---

## 5. Technical Requirements

* **Framework:** SvelteKit (Fast, reactive, no-bloat).
* **Styling:** TailwindCSS with `rounded-none` utility applied globally.
* **Fonts:** JetBrains Mono (Nerd Font patched for icons).
* **Backend:** A SvelteKit API route acting as a proxy to your Tailscale-linked Ollama instance.
* **Performance:** 0.0s transition times; all interactions must feel like a native terminal.

---

## 6. Project "Gama" Highlight (The "Flex")

The portfolio should specifically emphasize **Gama** because it represents your ability to build tools for other students.

* **Visual Idea:** A small "Code Playground" inside the portfolio where a user can see a snippet of `gama.h` code and see the resulting architecture diagram.

---

This sum covers every variable we discussed—from your age and your music to your specialized Rust projects and your Arch Linux workflow.

**Next Step:** Since you have the full spec now, would you like me to generate the **`tailwind.config.js`** and a basic **`Global.css`** that sets up your specific "Gruvbox-Dark" color palette and "Strictly Orthogonal" rules?
