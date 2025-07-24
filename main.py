from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal
from textual.widgets import Header, Footer, Static, TabbedContent, TabPane
from pyfiglet import Figlet

# --- Dev Icons (ASCII Art) ---
PYTHON_ICON = r"""
  .---.
 / o o \
 \  ^  /
  `---´
"""
GO_ICON = r"""
  ____
 /  _ \
|  / \ |
 \ \_/ /
  \___/
"""
DART_ICON = r"""
   /\
  /--\
 /____\
"""
FLUTTER_ICON = r"""
  _
 | |
 | |_
 |  _|
 |_|
"""
SVELTE_ICON = r"""
   ___
  / _ \
 | | | |
 | |_| |
  \___/
"""
LINUX_ICON = r"""
    .--.
   |o_o |
   |:_/ |
  //   \ \\
 (|     | )
/'\_   _/`\\
\___)=(___/
"""

# --- Figlet Title Generator ---
def create_title(text):
    figlet = Figlet(font='slant')
    return figlet.renderText(text)

class PortfolioApp(App):
    """A Textual portfolio app with improved UI/UX."""

    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Static("Hint: Use Tabs or Left/Right arrow keys to navigate.", classes="nav-hint")

        with TabbedContent(initial="home"):
            # --- Home Tab ---
            with TabPane("Home", id="home"):
                with VerticalScroll():
                    yield Static(create_title("ama"), classes="title")
                    yield Static("Engon Ken Morel", classes="subtitle")
                    yield Horizontal(
                        Container(
                            Static(
                                "Welcome to my digital space. I'm a student and software developer based in Yaounde, Cameroon. "
                                "I prefer the name [b]ama[/b]—a name I was drawn to for its inherent simplicity and symmetry. "
                                "It reflects my approach to both code and life: finding elegance in well-structured, balanced systems.",
                                classes="statement"
                            ),
                            Static(
                                "I am a core member of the [b]Record Breakers[/b], a team dedicated to creating technology that makes a tangible impact. "
                                "Our work is driven by the belief that thoughtful software can empower our local communities and create new opportunities for growth and learning.",
                                classes="statement"
                            ),
                            classes="card"
                        ),
                        classes="row row-center"
                    )

            # --- Dev Tab ---
            with TabPane("Dev", id="dev"):
                with VerticalScroll(classes="dev-container"):
                    yield Static(create_title("Dev World"), classes="title")
                    yield Horizontal(
                        Container(
                            Static("I thrive on the command line and am passionate about open-source technologies. My setup is my sanctuary, and my tools are extensions of my thinking. I primarily work on Linux, switching between the sleekness of Ubuntu Sway Remix and the raw focus of a TTY session. My editor is always [b]Neovim[/b]—it's where I build everything.", classes="statement"),
                            classes="card"
                        ),
                        classes="row row-center"
                    )

                    tech_stack = [
                        (GO_ICON, "[b]Go:[/b] My primary language for backend development. I appreciate its performance and concurrency model. I have experience building robust APIs with Gorilla Mux and am currently exploring Wails."),
                        (DART_ICON, "[b]Dart & Flutter:[/b] My go-to for mobile development. I've built and maintained Android applications with Flutter, leveraging its expressive UI framework to deliver high-quality user experiences."),
                        (PYTHON_ICON, "[b]Python:[/b] A versatile language I use for scripting, automation, and web development. Its vast ecosystem and readability make it an invaluable tool."),
                        (SVELTE_ICON, "[b]Svelte & SvelteKit:[/b] When I work on the web, I choose Svelte. I dislike the complexity of React/Next.js, and find Svelte's compiler-based approach more elegant."),
                        (LINUX_ICON, "[b]Julia & Others:[/b] I have a keen interest in scientific computing and data analysis, which is where Julia comes in. I'm also proficient in TypeScript for web projects."),
                    ]

                    for i, (icon, description) in enumerate(tech_stack):
                        alignment = "row-left" if i % 2 == 0 else "row-right"
                        
                        icon_widget = Static(icon, classes="dev-icon")
                        description_widget = Static(description, classes="skill-description")

                        # Alternate the order of widgets based on the row
                        if i % 2 == 0: # Even row (left-aligned card), icon is on the left
                            widgets = [icon_widget, description_widget]
                        else: # Odd row (right-aligned card), icon is on the right
                            widgets = [description_widget, icon_widget]
                            icon_widget.add_class("dev-icon-right") # Add class to adjust margin

                        yield Horizontal(
                            Container(
                                Horizontal(*widgets, classes="skill-block"),
                                classes="card"
                            ),
                            classes=f"row {alignment}"
                        )

            # --- Experience Tab ---
            with TabPane("Experience", id="experience"):
                with VerticalScroll():
                    yield Static(create_title("Experience"), classes="title")
                    yield Horizontal(
                        Container(
                            Static("Record Breakers (rbs.cm)", classes="subtitle"),
                            Static(
                                "At Record Breakers, my role is twofold. As a [b]Core Backend Developer[/b], I architect and build server-side logic using Go. As an [b]Android Developer[/b], I use Dart and Flutter to create mobile frontends. My most significant contribution has been to our flagship project, [b]IS (Intranet of Schools)[/b]. This mobile platform is designed to bridge the technology gap in our local educational institutions. It's a project I'm incredibly proud of. (is.rbs.cm)",
                                classes="statement"
                            ),
                            classes="card"
                        ),
                        classes="row row-center"
                    )
                    yield Horizontal(
                        Container(
                            Static("Competitive Achievements", classes="subtitle"),
                            Static(
                                "I believe that competition is a catalyst for growth. With my team, The Record Breakers, I've had the opportunity to test our skills and ideas in high-pressure environments:",
                                classes="statement"
                            ),
                            Static("- [b]The Tech Inovation Challenge 2025:[/b] We were honored to receive third place for our work on 'IS'.", classes="list-item"),
                            Static("- [b]ICT University Tech Innovation Challenge 2025:[/b] A valuable learning experience that sharpened our problem-solving skills.", classes="list-item"),
                            classes="card"
                        ),
                        classes="row row-center"
                    )

            # --- Contact Tab ---
            with TabPane("Contact", id="contact"):
                with VerticalScroll():
                    yield Static(create_title("Connect"), classes="title")
                    yield Horizontal(
                        Container(
                            Static("I'm passionate about my work and always looking to connect with like-minded people. In my downtime, you'll find me unwinding with anime or a film on Netflix or Crunchyroll.", classes="statement"),
                            classes="card"
                        ),
                        classes="row row-center"
                    )
                    yield Horizontal(
                        Container(
                            Static("[b]Personal Email:[/b] engonken8@gmail.com", classes="list-item"),
                            Static("[b]Work Email:[/b] engon@rbs.cm", classes="list-item"),
                            Static("[b]Phone:[/b] +237 670570039", classes="list-item"),
                            classes="card"
                        ),
                        classes="row row-center"
                    )

        yield Footer()

if __name__ == "__main__":
    app = PortfolioApp()
    app.run()