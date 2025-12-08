# How to Use Colors in GitHub READMEs

This guide demonstrates various ways to add color and formatting to your GitHub README files.

---

## 📋 Table of Contents

1. [Text Highlighting with `diff`](#text-highlighting-with-diff)
2. [Text Color with LaTeX](#text-color-with-latex)
3. [Applying to Titles and Text](#applying-to-titles-and-text)
4. [Limitations](#limitations)

---

## Text Highlighting with `diff`

Use `diff` syntax to highlight entire lines. Perfect for drawing attention to specific content.

```diff
- This text is highlighted in red.
+ This text is highlighted in green.
! This text is highlighted in orange.
# This text is in gray.
@@ This text is in purple (and bold). @@
```

---

## Text Color with LaTeX

For precise color control, use LaTeX syntax to color individual words or phrases.

### Basic Syntax

```
$$\color{colorname}\textrm{Your text}$$
```

**Example:**
```
$$\color{orange}\textrm{This is a short-term goal.}$$
```

**Renders as:**
$$\color{orange}\textrm{This is a short-term goal.}$$

### Available Colors

| Color | Preview |
|-------|---------|
| Red | $${\color{red}Red}$$ |
| Green | $${\color{green}Green}$$ |
| Light Green | $${\color{lightgreen}Light Green}$$ |
| Blue | $${\color{blue}Blue}$$ |
| Light Blue | $${\color{lightblue}Light Blue}$$ |
| Yellow | $${\color{yellow}Yellow}$$ |
| Orange | $${\color{orange}Orange}$$ |
| Purple | $${\color{purple}Purple}$$ |
| Pink | $${\color{pink}Pink}$$ |
| Brown | $${\color{brown}Brown}$$ |
| Gray | $${\color{gray}Gray}$$ |
| Black | $${\color{black}Black}$$ |

### Multiple Colors in One Line

Combine multiple colors in a single line using `\space` to separate them.

**Example 1:**
```
$${\color{red}Welcome \space \color{lightblue}To \space \color{orange}Stackoverflow}$$
```
$${\color{red}Welcome \space \color{lightblue}To \space \color{orange}Stackoverflow}$$

**Example 2:**
```
$${\color{red}Welcome \space \color{lightblue}To \space \color{lightgreen}Github}$$
```
$${\color{red}Welcome \space \color{lightblue}To \space \color{lightgreen}Github}$$

---

## Applying to Titles and Text

### Colored Titles

**Main Title:**
```
# $${\color{blue}This \space is \space a \space Main \space Title}$$
```
# $${\color{blue}This \space is \space a \space Main \space Title}$$

**Subtitle:**
```
## $${\color{green}This \space is \space a \space Subtitle}$$
```
## $${\color{green}This \space is \space a \space Subtitle}$$

### Text Formatting

By default, text within `$$...$$` is *italic*. Use `\textrm{}` for normal (roman) text.

| Style | Syntax | Result |
|-------|--------|--------|
| Italic (Default) | `$${\color{red}This \space is \space italic}$$` | $${\color{red}This \space is \space italic}$$ |
| Normal (Roman) | `$$\color{orange}\textrm{This is normal text.}$$` | $$\color{orange}\textrm{This is normal text.}$$ |

---

## Limitations

⚠️ **Bold Text:** Standard Markdown bold (`**...**`) does not work inside `$$...$$` blocks. There is currently no reliable, cross-platform method to make colored text **bold** within GitHub's Markdown using LaTeX.

If you have a working solution, please open an issue or submit a pull request!
