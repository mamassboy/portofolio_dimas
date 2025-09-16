import { useState } from "react";
import "./index.css";

export default function App() {
  const [tabNames, setTabNames] = useState([
    "Why React?",
    "Core Features",
    "Related Resources",
    "Dream Future"
  ]);

  const [tabContent, setTabContent] = useState([
    [
      "React sangat populer",
      "React membuat UI kompleks jadi mudah",
      "Sangat kuat dan fleksibel",
      "Ekosistem aktif & serbaguna"
    ],
    ["Components, JSX & Props", "State", "Hooks", "Dynamic rendering"],
    ["React.dev", "Next.js", "React Native"],
    ["Lulus 3,5 tahun", "Punya penghasilan 15 juta", "Umrohkan orang tua"]
  ]);

  const [activeContentIndex, setActiveContentIndex] = useState(0);
  const [newTabName, setNewTabName] = useState("");
  const [newItem, setNewItem] = useState("");

  // ➕ Fungsi menambah tab baru
  const addTabHandler = () => {
    if (!newTabName.trim()) return; // kalau kosong, jangan diproses
    setTabNames([...tabNames, newTabName]); // tambah nama tab
    setTabContent([...tabContent, []]); // kasih array kosong untuk isi tab
    setNewTabName(""); // reset input
  };

  // ➕ Fungsi menambah item ke tab aktif
  const addItemHandler = () => {
    if (!newItem.trim()) return; // jangan proses kalau kosong
    const updatedContent = [...tabContent];
    updatedContent[activeContentIndex] = [
      ...updatedContent[activeContentIndex],
      newItem
    ];
    setTabContent(updatedContent);
    setNewItem("");
  };

  return (
    <>
      <header>
        <img src="logo512.png" alt="React logo" />
        <h1>React.js</h1>
        <p>i.e., using the React library for rendering the UI</p>
      </header>

      <div id="tabs">
        <menu>
          {tabNames.map((tab, index) => (
            <button
              key={tab}
              className={activeContentIndex === index ? "active" : ""}
              onClick={() => setActiveContentIndex(index)}
            >
              {tab}
            </button>
          ))}
        </menu>

        {/* Form tambah tab */}
        <div style={{ margin: "1rem 0" }}>
          <input
            type="text"
            value={newTabName}
            onChange={(e) => setNewTabName(e.target.value)}
            placeholder="Nama tab baru..."
          />
          <button onClick={addTabHandler}>Add Tab</button>
        </div>

        <div id="tab-content">
          <ul>
            {tabContent[activeContentIndex].map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>

          {/* Form Tambah Item */}
          <div style={{ marginTop: "1rem" }}>
            <input
              type="text"
              value={newItem}
              onChange={(e) => setNewItem(e.target.value)}
              placeholder="Tambah item baru..."
            />
            <button onClick={addItemHandler}>Add Item</button>
          </div>
        </div>
      </div>
    </>
  );
}
