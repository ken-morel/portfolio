from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, TabbedContent, TabPane
from textual.containers import Container, VerticalScroll

AMA_ART = r"""
      ___       ___       ___     
     /  /\\     /  /\\     /  /\\    
    /  /:/_   /  /::\\   /  /::\\   
   /  /:/ /\\ /  /:/\\:\ /  /:/\\:\  
  /  /:/ /://  /:/  \\://  /:/  \\:\ 
 /__/:/ /://__/:/ \__\\://__/:/ \__\\:
 \\  \\:\/:/ \\  \\:\ /  / \\  \\:\ /  /
  \\  \\::/   \\  \\:\  /   \\  \\:\  / 
   \\  \\:\    \\  \\:\ /     \\  \\:\ /  
    \\  \\:\    \\  \\:\       \\  \\:\  
     \\__\\/     \\__\\/        \\__\\/
"""

ENGON_KEN_MOREL_ART = r"""
______ _   _  ____  _   _  _   _    _  __ _   _      _    ____  _____  ______   _ 
|  ____| \\ | |/ __ \\| \\ | |/ __ \\  | |/ /| \\ | |    | |  / __ \\|  __ \\|  ____| | |
| |__  |  \\| | |  | |  \\| | |  | | | ' / |  \\| |    | | | |  | | |__) | |__    | |
|  __| | . ` | |  | | . ` | |  | | |  <  | . ` |_   | | | |  | |  _  /|  __|   |_|
| |____| |\\  | |__| | |\\  | |__| | | . \\ | |\\  | |__| | | |__| | | \\ \\| |____   _ 
|______|_| \\_|\\____/|_| \\_|\\____/  |_|\\_\\|_| \\_|\\____/   \\____/|_|  \\_\\\\______| |_|
"""


class PortfolioApp(App):
    """A Textual portfolio app."""

    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with TabbedContent(initial="about"):
            with TabPane("About", id="about"):
                with VerticalScroll():
                    yield Static(ENGON_KEN_MOREL_ART, id="title")
                    yield Static(AMA_ART, id="subtitle")
                    yield Static("Full Name: Engon Ken Morel")
                    yield Static("Preferred Name: ama")
                    yield Static("Location: Yaounde, Cameroon")
                    yield Static("Occupation: Student & Core Backend Developer at Record Breakers")
            with TabPane("Skills", id="skills"):
                with VerticalScroll():
                    yield Static("[b]Languages:[/b] Go, Dart, Julia, Python, TypeScript")
                    yield Static("[b]Frameworks:[/b] Flutter, Svelte, SvelteKit, Gorilla")
                    yield Static("[b]Other:[/b] Wails (learning), Linux (Ubuntu Sway Remix/TTY), Neovim")
            with TabPane("Projects", id="projects"):
                with VerticalScroll():
                    yield Static("[b]IS - Intranet of Schools[/b]")
                    yield Static("A mobile application to empower education in our local community.")
                    yield Static("Homepage: is.rbs.cm")
            with TabPane("Experience", id="experience"):
                with VerticalScroll():
                    yield Static("[b]Record Breakers[/b] (rbs.cm)")
                    yield Static("Core Backend Developer (Go)")
                    yield Static("Android Developer (Dart & Flutter)")
                    yield Static("\n[b]Competitions:[/b]")
                    yield Static("The Tech Inovation Challenge 2025: 3rd Place (with Record Breakers)")
                    yield Static("ICT University Tech Innovation Challenge 2025: Participant (with Record Breakers)")
            with TabPane("Contact", id="contact"):
                with VerticalScroll():
                    yield Static("Personal Email: engonken8@gmail.com")
                    yield Static("Work Email: engon@rbs.cm")
                    yield Static("Phone: +237 670570039")
                    yield Static("Emojis: Traditional :-)")
        yield Footer()

if __name__ == "__main__":
    app = PortfolioApp()
    app.run()