const BASE_URL = "";

function handleErrors(response) {
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response;
}

export function getMemes() {
  return window
    .fetch(`${BASE_URL}/memes/`)
    .then(handleErrors)
    .then((r) => r.json());
}

export function postMeme(data) {
  return window
    .fetch(`${BASE_URL}/memes/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
    .then(handleErrors)
    .then((r) => r.json());
}

export function updateMeme(memeId, { url, caption }) {
  return window
    .fetch(`${BASE_URL}/memes/${memeId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url, caption }),
    })
    .then(handleErrors)
    .then((r) => r.json());
}
