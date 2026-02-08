<script lang="ts">
  import SpotifyLogo from "$lib/assets/spotify.svg";

  // Placeholder for the scrolling marquee text
  let nowPlaying = "Richard Bona - Te Dikalo";
</script>

<div class="spotify-widget">
  <img class="spotify-icon" src={SpotifyLogo} alt="Spotify" />
  <div class="spotify-text-container">
    <span class="now-playing-text">{nowPlaying}</span>
  </div>
</div>

<style lang="sass">
.spotify-widget
  display: flex
  align-items: center
  height: 100%
  padding: 0 10px
  overflow: hidden // Important for marquee effect later

.spotify-icon
  width: 18px
  height: 18px
  margin-right: 8px
  flex-shrink: 0

.spotify-text-container
  white-space: nowrap
  overflow: hidden
  
.now-playing-text
  color: #ebdbb2 // Gruvbox foreground
  font-size: 14px
  // A marquee animation can be added here later
  // animation: marquee 15s linear infinite;

// @keyframes marquee
//   0%
//     transform: translateX(100%)
//   100%
//     transform: translateX(-100%)
</style>
