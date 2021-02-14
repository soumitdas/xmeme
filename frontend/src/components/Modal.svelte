<!-- Ref: https://dev.to/vibhanshu909/how-to-create-a-full-featured-modal-component-in-svelte-and-trap-focus-within-474i -->
<script>
  export let isOpen = false

  function open() {
    isOpen = true
  }
  function close() {
    isOpen = false
  }
</script>

<style>
  div.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;
  }
  div.backdrop {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    z-index: 1040;
  }
  div.content-wrapper {
    z-index: 1100;
    max-width: 70vw;
    border-radius: 0.3rem;
    background-color: var(--black);
    overflow: hidden;
  }
  div.content {
    max-height: 80vh;
    overflow: auto;
  }
</style>

<slot name="trigger" {open}>
  
</slot>

{#if isOpen}
  <div class="modal">
    <div class="backdrop" on:click={close} />

    <div class="content-wrapper">
      <div class="content">
          <slot name="content" {close} />
      </div>
    </div>
  </div>
{/if}