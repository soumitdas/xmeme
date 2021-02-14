<script>
  import {isModalOpen, modalFormData} from "../store"

  function handleClick() {
    isModalOpen.set(true)
    modalFormData.set(undefined)
  }
</script>

<style>
  .navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin: 2rem 0;
  }

  .navbar-brand span {
    font-weight: 600;
    font-size: 3.3rem;
  }
</style>

<div class="navbar">
  <div class="navbar-left">
    <div class="navbar-brand">
      <span>XMeme</span>
    </div>
  </div>
  <div class="navbar-right">
    <button class="btn btn-green" on:click={handleClick}>Add Meme</button>
  </div>
</div>