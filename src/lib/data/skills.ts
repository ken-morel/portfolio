// src/lib/data/skills.ts

export interface Skill {
  name: string;
  proficiency: number; // A value from 0 to 100
  color: string;
}

export interface Achievement {
  year: number;
  event: string;
  role: string;
}

// Memory Usage: Your proficiency in programming languages
export const languages: Skill[] = [
  { name: "Rust", proficiency: 90, color: "#dea584" },
  { name: "C", proficiency: 80, color: "#56949f" },
  { name: "Go", proficiency: 75, color: "#73c991" },
  { name: "Julia", proficiency: 60, color: "#a074c4" },
  { name: "V", proficiency: 50, color: "#8a9096" },
  { name: "TypeScript", proficiency: 85, color: "#4e8fdd" },
];

// Running Tasks: Your experience and significant events
export const achievements: Achievement[] = [
  { year: 2025, event: "TIC Summit", role: "Record Breaker" },
  { year: 2024, event: "Hack Club Daydream", role: "Organizer" },
  // Add more achievements here
];

// Network: Social links
export const socialLinks = {
  GitHub: "https://github.com/ken-morel",
  LinkedIn: "https://linkedin.com/in/engon-morel",
  Discord: "ken.morel", // Your Discord username
};
