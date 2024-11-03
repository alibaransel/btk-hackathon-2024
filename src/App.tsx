import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Header } from './components/Header';
import { StoriesPage } from './pages/StoriesPage';
import { StoryPage } from './pages/StoryPage';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50">
        <Header />
        <Routes>
          <Route path="/" element={<StoriesPage />} />
          <Route path="/story/:id" element={<StoryPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;