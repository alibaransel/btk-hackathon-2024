import React from 'react';
import { Link } from 'react-router-dom';
import { Clock, User } from 'lucide-react';
import { Story } from '../types';

interface StoryCardProps {
  story: Story;
}

export function StoryCard({ story }: StoryCardProps) {
  return (
    <Link
      to={`/story/${story.id}`}
      className="bg-white rounded-lg shadow-md overflow-hidden transition-transform hover:scale-[1.02] hover:shadow-lg"
    >
      <div className="h-48 w-full overflow-hidden">
        <img
          src={story.coverImage}
          alt={story.title}
          className="w-full h-full object-cover"
        />
      </div>
      <div className="p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-2">{story.title}</h2>
        <p className="text-gray-600 mb-4">{story.excerpt}</p>
        <div className="flex items-center text-sm text-gray-500 space-x-4">
        <div className="flex items-center">

          </div>
          <div className="flex items-center">
            <Clock className="h-4 w-4 mr-1" />
            {story.readTime}
          </div>
        </div>
      </div>
    </Link>
  );
}