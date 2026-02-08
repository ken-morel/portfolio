<div class="background"></div>
Hello

<style lang="scss">
  div.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1; // Ensure it stays behind other content

    // Gruvbox Dark background with subtle grid lines
    background-color: #282828; // Gruvbox dark background
    background-image:
      linear-gradient(0deg, transparent 99%, #3c3836 100%),
      // Subtle dark grey lines
      linear-gradient(90deg, transparent 99%, #3c3836 100%);
    background-size: 20px 20px; // Size of the grid cells
    background-attachment: fixed;
  }
</style>
