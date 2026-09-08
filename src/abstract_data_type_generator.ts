// src/contributors_page.ts
'use client'; // Required for React/Next.js interactive Easter Eggs and animations

export default function ContributorsPage() {
  const [activeTab, setActiveTab] = useState<'all' | 'agents'>('all');

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-950 to-black text-white overflow-hidden">
      {/* HEADER */}
      <header className="relative z-10 border-b border-gold-600/30 backdrop-blur-md sticky top-0 transition-all duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <span className="text-gold-500 font-bold tracking-wide text-lg animate-pulse">AgentPipe</span>
            <nav className="hidden md:flex gap-6">
              {['Home', 'Contributors'].map((item) => (
                <a key={item} href={`#${item.toLowerCase()}`} onClick={() => setActiveTab(item as any)} className="text-sm text-gray-300 hover:text-gold-400 transition-colors relative group" aria-label={item}>
                  {item === 'Home' ? 'Welcome Back!' : item.toUpperCase()} 
                  <span className="absolute -bottom-1 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-purple-500 to-transparent"></span>
                </a>
              ))}
            </nav>
          </div>

          {/* HERO SECTION */}
          <section id="home" className="relative z-10 flex items-center justify-center h-full min-h-[40vh] text-gold-50">
            <img 
              src="https://images.unsplash.com/photo-1628739910217-cf1dcaad6e4a?q=80&w=1974&auto=format&fit=crop" // Placeholder for corporate goose image (using generic goose stock)
              alt="Corporate Goose People Working in a Factory" 
              className="max-w-full max-h-[50vh] object-contain rounded-lg shadow-2xl border-b-8 border-gold-600/30 transition-all duration-700 ease-in-out hover:scale-[1.02]"
            />
          </section>

          {/* EASTER EGGS */}
          <div className="absolute top-4 right-4 z-20 hidden md:block">
             <img 
              src="https://images.unsplash.com/photo-1537649859605-ea0b9f8dcaae?q=80&w=2670&auto=format&fit=crop" // Placeholder for golden egg 1 (mischievous)
              alt="Golden Egg Mischievous Agent" 
              className="shadow-[inset_4px_4px_0_rgba(0,0,0,0.5)] animate-pulse-slow hover:scale-125 transition-transform duration-300"
            />
          </div>

          <img 
             src="https://images.unsplash.com/photo-1629784721686-cbcbdaa9dfe2?q=80&w=2670&auto=format&fit=crop" // Placeholder for golden egg 2 (grumpy)
             alt="Golden Egg Grumpy Agent" 
             className="shadow-[inset_4px_4px_0_rgba(0,0,0,0.5)] animate-pulse-slow hover:scale-125 transition-transform duration-300"
          />

          <div className="absolute bottom-8 right-8 z-20 hidden md:block">
             <img 
              src="https://images.unsplash.com/photo-1649723374336-fc3d5e5a2fdd?q=80&w=2670&auto=format&fit=crop" // Placeholder for golden egg 3 (stressed)
              alt="Golden Egg Stressed Agent" 
              className="shadow-[inset_4px_4px_0_rgba(0,0,0,0.5)] animate-pulse-slow hover:scale-125 transition-transform duration-300"
            />
          </div>

           {/* FOOTER */}
           <footer className="relative z-10
