# How to Use Colors in GitHub READMEs

This guide demonstrates various ways to add color and formatting to your GitHub README files.

## Text Highlighting with `diff`

You can use `diff` syntax within a code block to highlight entire lines of text. This is useful for drawing attention to specific lines.

```diff
- This text is highlighted in red.
+ This text is highlighted in green.
! This text is highlighted in orange.
# This text is in gray.
@@ This text is in purple (and bold). @@
```

## Text Color with LaTeX

For more control over text color, you can use LaTeX syntax. This allows you to color individual words or phrases.

### Basic Usage

The basic syntax is `$$\color{colorname}\textrm{Your text}$$`.

**Example:**

`$$\color{orange}\textrm{This is a short-term goal.}$$`

This will be rendered as:
$$\color{orange}\textrm{This is a short-term goal.}$$

### Available Colors

Here are some of the colors you can use:

- $${\color{red}Red}$$
- $${\color{green}Green}$$
- $${\color{lightgreen}Light Green}$$
- $${\color{blue}Blue}$$
- $${\color{lightblue}Light Blue}$$
- $${\color{yellow}Yellow}$$
- $${\color{orange}Orange}$$
- $${\color{purple}Purple}$$
- $${\color{pink}Pink}$$
- $${\color{brown}Brown}$$
- $${\color{gray}Gray}$$
- $${\color{black}Black}$$

### Multiple Colors in One Line

You can combine multiple colors in a single line.

**Example:**

`$${\color{red}Welcome \space \color{lightblue}To \space \color{orange}Stackoverflow}$$`

This will be rendered as:
$${\color{red}Welcome \space \color{lightblue}To \space \color{orange}Stackoverflow}$$

Another example:
`$${\color{red}Welcome \space \color{lightblue}To \space \color{lightgreen}Github}$$`

This will be rendered as:
$${\color{red}Welcome \space \color{lightblue}To \space \color{lightgreen}Github}$$

## Applying to Titles and Text

You can use these coloring methods for titles, subtitles, and regular text.

### Colored Titles

`# $${\color{blue}This \space is \space a \space Main \space Title}$$`
# $${\color{blue}This \space is \space a \space Main \space Title}$$

`## $${\color{green}This \space is \space a \space Subtitle}$$`
## $${\color{green}This \space is \space a \space Subtitle}$$

### Text Formatting (Normal vs. Italic)

By default, text within the `$$...$$` block is rendered in an *italic* math font. To get normal (non-italic, or "roman") text, you need to use the `\textrm{}` command.

- **Italic (Default):**
  `$${\color{red}This \space is \space italic}$$`
  $${\color{red}This \space is \space italic}$$

- **Normal (Roman):**
  `$$\color{orange}\textrm{This is normal text.}$$`
  $$\color{orange}\textrm{This is normal text.}$$


### A Note on Bold Text
Standard Markdown bold (`**...**`) does not work on text inside a `$$...$$` block. After numerous tests, it appears there is currently no reliable, cross-platform method to make $$\color{orange}\textrm{colored}$$ text **bold** within GitHub's Markdown using LaTeX.
If you know of a working solution, please feel free to open an issue or submit a pull request!
