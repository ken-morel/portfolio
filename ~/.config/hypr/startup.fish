#!/usr//bin/fish

# --- Hyprland Aliases & Functions ---
alias hypr 'hyprctl dispatch'
alias workspace 'hypr workspace'
function hexec
    hypr exec "$argv"
end

# --- Tmux Setup ---
# On boot, we just tell the continuum plugin to restore ALL saved sessions.
# This will bring back 'terminals', 'editors', 'monitors', etc. if they existed.
~/.config/tmux/plugins/tpm/scripts/continuum_restore.sh || true

# --- Hyprland Workspace "Viewers" ---
# The logic for each workspace is now identical:
# 1. Go to the workspace.
# 2. Launch a Ghostty terminal.
# 3. Tell that terminal to attach to a SPECIFIC named session.
#    The `new-session -A -s <name>` part is crucial:
#    - It Attaches if the session exists.
#    - It Creates it if it does not exist.
# This makes the script work perfectly on both a fresh boot and a restore.

workspace 1
# This terminal becomes the viewport for the 'terminals' session.
hexec ghostty -e tmux new-session -A -s terminals

sleep 1

workspace 2
# This terminal becomes the viewport for the 'editors' session.
hexec ghostty -e tmux new-session -A -s editors

sleep 1

workspace 3
# Graphical apps are unchanged.
hexec qutebrowser

sleep 1

workspace 5
# This terminal becomes the viewport for the 'files' session.
hexec ghostty -e tmux new-session -A -s files

# --- Special Workspace for Monitors ---
# This follows the exact same pattern.
special music
hexec ghostty -e tmux new-session -A -s monitors
sleep 3
special music # Close the special workspace

# Return to a default workspace at the end
workspace 1