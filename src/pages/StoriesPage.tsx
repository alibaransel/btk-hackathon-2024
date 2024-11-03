import React from 'react';
import { stories } from '../data/stories';
import { StoryCard } from '../components/StoryCard';

export function StoriesPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Hayat Fakültesi'ne Hoşgeldiniz!</h1>
          <p className="text-xl text-gray-600">Gemini api ile ilkokul çocuklarına yönelik öğretici hikayeler</p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {stories.map((story) => (
            <StoryCard key={story.id} story={story} />
          ))}
        </div>
      </div>
    </div>
  );
}