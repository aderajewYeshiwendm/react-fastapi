import { useEffect, useState } from "react";

function App() {
  const [content, setContent] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((response) => response.text()) // Get raw HTML response
      .then((data) => setContent(data))
      .catch((error) => console.error("Error fetching:", error));
  }, []);

  return (
    <div>
      <h1>FastAPI + React (Website embedding)</h1>
      <iframe
        srcDoc={content}
        style={{ width: "100%", height: "100vh", border: "none" }}
      />
    </div>
  );
}

export default App;
