<script>
  import {memeList} from "../store"
  import {postMeme, updateMeme} from "../api"

  export let onCancel = () => {};
  export let isEditing = false;
  export let formData = {
    name: "",
    url: "",
    caption: ""  
  }

  let newFormData = {...formData}

  let isLoading = false
  let error = null

  $: hasFormChanged = JSON.stringify(formData) !== JSON.stringify(newFormData)

  function handleInput(e) {
    newFormData[e.target.name] = e.target.value
  }

  const isValidUrl = (url) => {
    try {
      new URL(url);
    } catch (e) {
      return false;
    }
    return true;
  };

  async function handleSubmit() {
    if (!isValidUrl(newFormData.url)) {
      error = "Invalid URL"
      return
    }

    try {
      isLoading = true
      if (isEditing) {
        const resp = await updateMeme(newFormData.id, newFormData)
        memeList.update(prevList => {
          const indexOfMemeToBeUpdated = prevList.findIndex(val => val.id === newFormData.id)
          if (indexOfMemeToBeUpdated > -1) {
            prevList[indexOfMemeToBeUpdated] = resp
            return [...prevList]
          } else {
            return prevList
          }
        })
      } else {
        const resp = await postMeme(newFormData)
        memeList.update(prevList => [resp, ...prevList])
      }
      isLoading = false
      onCancel()
    } catch (e) {
      error = e.message
      isLoading = false
    }
  }
</script>

<style>
  .form {
    margin: 0 1rem;
    padding: 2rem;
    width: 60vw;
  }

  .buttons {
    text-align: right;
    margin-top: 2rem;
  }
</style>

<form class="form" on:submit|preventDefault={handleSubmit}>
  <h2>{isEditing ? "Update" : "New"} Post</h2>
  {#if error}
    <h4 style="color: red;">{error}</h4>
  {/if}
  <label for="name">Name</label>
  <input type="text" name="name" placeholder="Your Name" bind:value={newFormData.name} on:input={handleInput} required disabled={isEditing} maxlength="30">
  <label for="url">URL</label>
  <input type="text" name="url" placeholder="Meme url" bind:value={newFormData.url} on:input={handleInput} required>
  <label for="caption">Caption</label>
  <input type="text" name="caption" placeholder="Caption" bind:value={newFormData.caption} on:input={handleInput} required maxlength="300">
  <div class="buttons">
    <button class="btn btn-blue" disabled={isLoading | !hasFormChanged}>{isLoading ? "Loading..." : isEditing ? "Update" : "Post"}</button>
    <button class="btn btn-red" on:click={onCancel} disabled={isLoading}>Cancel</button>
  </div>
</form>