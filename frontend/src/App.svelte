<script>
  import { onMount } from 'svelte';
  import Modal from "./components/Modal.svelte"
  import Navbar from "./components/Navbar.svelte"
  import MemeCard from "./components/MemeCard.svelte"
  import MemeForm from "./components/MemeForm.svelte"
  import { getMemes } from "./api"
  import { memeList, isModalOpen, modalFormData } from "./store"

  $: isEditing = $modalFormData && typeof $modalFormData === "object"

  onMount(() => {
    getMemes().then(resp => memeList.set(resp)).catch(e => console.log(e.message))
  })

</script>

<style>
  .meme-container {
    --gap: 2rem;
    display: flex;
    flex-wrap: wrap;
    margin: calc(-1 * var(--gap)) 0 0 calc(-1 * var(--gap));
    /* width: calc(100% + var(--gap)); */
    /* align-items: ; */
    max-width: 500px;
    margin: 0 auto;
  }

  .meme-container > * {
    margin: var(--gap) 0 0 var(--gap);
  }

  .meme-item {
    flex: 1 1 100%
  }
</style>

<div class="wrapper">
	<header>
		<div class="container">
      <Navbar />
		</div>
	</header>
	<main>
    <div class="container">
      <div class="meme-container">
        {#each $memeList as meme}
        <div class="meme-item">
          <MemeCard cardData={meme} />
        </div>
        {/each}
      </div>
    </div>
  </main>
</div>
<Modal bind:isOpen={$isModalOpen}>
  <div slot="content" let:close>
    <MemeForm isEditing={isEditing} onCancel={close} formData={$modalFormData} />
  </div>
</Modal>
<footer>
  <div class="footer">Made with ❤️ by <a href="https://www.soumitdas.com/" target="_blank" rel="noopener noreferrer">Soumit</a></div>
</footer>
