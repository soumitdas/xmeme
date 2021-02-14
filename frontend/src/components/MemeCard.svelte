<script>
  import {isModalOpen, modalFormData} from "../store"
  import {dateToMonDDYYYYHHMMAP} from "../helpers/date"

  export let cardData = {
    name: "",
    url: "",
    caption: ""    
  }

  function openModal() {
    isModalOpen.set(true);
    modalFormData.set(cardData);
  }
</script>

<style>
  .card {
    display: flex;
    flex-direction: column;

    /* padding: 2rem; */
    justify-content: space-between;

    border-radius: 5px;
    background: var(--grey);
  }

  .card img {
    border-top-right-radius: 5px;
    border-top-left-radius: 5px;
  }

  .card-content {
    padding: 2rem;
    font-size: var(--font-size-small);
  }

  .card-content-header {
    font-size: 0.75em;
  }

  .card-content-author {
    font-size: 1.5em;
    font-weight: 700;
  }

  .card-content-caption {
    margin: 1rem 0 2rem;
  }

  .card-content-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }
</style>

<div class="card">
  <img src={cardData.url} alt={cardData.caption} onerror="this.onerror=null;this.src='/images/no-image.png';">
  
  <div class="card-content">
    <div class="card-content-header">
      <p class="card-content-author">{cardData.name}</p>
      <p>{dateToMonDDYYYYHHMMAP(cardData.createdAt)}</p>
    </div>
    <p class="card-content-caption">{cardData.caption}</p>
    <button class="btn btn-blue" on:click={openModal}>Edit</button>
  </div>
</div>