import { useState } from 'react'

import './App.css'

function App() {
  

  return (
    <form
        onSubmit={handleSubmit}
        encType="multipart/form-data"
    >
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setImage(e.target.files[0])}
        />
        <button type="submit">Submit</button>
        {(imageLoading)&& <p>Loading...</p>}
    </form>
)
}

export default App
