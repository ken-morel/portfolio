<script lang="ts">
  import SpotifyLogo from "$lib/assets/spotify.svg";
</script>

<div class="tray-widget">
  <img class="tray-icon" src={SpotifyLogo} alt="S" />
  <div class="spotify-view"></div>
</div>

<style lang="sass">
.tray-widget
  margin: 10px auto
  align-items: center
  position: relative
  width: fit-content
  .tray-icon
    width: 15px
    margin: auto
  .spotify-view
    position: absolute
    top: 0
    left: 0
    width: 200px
    height: 150px
    border: 1px dark-grey solid
    background-color: #5558
    backdrop-filter: blur(5px)
    display: none
  &:hover
    .spotify-view
      display: block
</style>
