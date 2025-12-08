# How to Use Colors in GitHub READMEs

This guide demonstrates various ways to add color and formatting to your GitHub README files.

---


## 📋 Table of Contents

1. [Text Highlighting with `diff`](#text-highlighting-with-diff)
2. [Text Color with LaTeX](#text-color-with-latex)
3. [Text Alignment](#text-alignment)
4. [Applying to Titles and Text](#applying-to-titles-and-text)
5. [Limitations](#limitations)

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
$\color{colorname}\textrm{Your text}$
```

**Example:**
```
$\color{orange}\textrm{This is an orange Example.}$
```

**Renders as:**
$\color{orange}\textrm{This is an orange Example.}$

---
### Available Colors

| Preview |Preview|
|---------|-------|
 $\color{red}\textrm{red}$       | $\color{green}\textrm{green}$
 $\color{green}\textrm{green}$   | $\color{lightgreen}\textrm{lightgreen}$ |
 $\color{blue}\textrm{blue}$     | $\color{lightblue}\textrm{lightblue}$ |
 $\color{yellow}\textrm{yellow}$ | $\color{orange}\textrm{orange}$ |
 $\color{purple}\textrm{purple}$ | $\color{pink}\textrm{pink}$ |
 $\color{brown}\textrm{brown}$   | $\color{gray}\textrm{gray}$ |
 $\color{black}\textrm{black}$   

### Multiple Colors in One Line

Combine multiple colors in a single line:

**Example:**
```
${\textrm{\color{red}This \color{lightblue}Text has \color{orange}multiple colors}}$
```
**Renders as:**
${\textrm{\color{red}This \color{lightblue}Text has \color{orange}multiple colors}}$


### Text Alignment

You can control the alignment of colored text using different LaTeX syntax:

**Left-aligned (using single `$...$`):**
```
${\textrm{\color{orange}This is left aligned}}$
```
${\textrm{\color{orange}This is left aligned}}$

**Center-aligned (using double `$$...$$`):**
```
$${\textrm{\color{orange}This is center-aligned}}$$
```
$${\textrm{\color{orange}This is center-aligned}}$$

---

## Applying to Titles and Text

### Colored Titles

**Main Title:**
```
# ${\color{blue}This is a Main Title}$
```
# ${\textrm{\color{blue}This is a Main Title}}$

**Subtitle:**
```
## $${\color{green}This is a Subtitle}$$
```
## ${\textrm{\color{green}This is a Subtitle}}$

### Text Formatting

By default, text is *italic*. Use `\textrm{}` for normal (roman) text.

| Style | Syntax | Result |
|-------|--------|--------|
| Italic (Default) | `$${\color{red}This \space text \space is \space italic}$$` | $${\color{red}This \space text \space is \space italic}$$ |
| Normal (Roman) | `$$\color{orange}\textrm{This text is normal.}$$` | $$\color{orange}\textrm{This text is normal.}$$ |

### Important Note: if you use Italic , you have to use \space for seperating words

### Combination 
 Here are some examples of how to combine them:

## ${\textrm{\color{red}This \color{pink}text contains \color{orange}several colors,} \color{lightgreen}\space is \space a \space subheading, \space and \space is \space half \space written \space in \space italic.}$ ##
 ```
## ${\textrm{\color{red}This \color{pink}text contains \color{orange}several colors,} \color{lightgreen}\space is \space a \space subheading, \space and \space is \space half \space written \space in \space italic.}$ ##
 ```




## You can also  ${\textrm{\color{orange}color individual \color{lightgreen} words in the middle }}$ of a sentence.
```
## You can also  ${\textrm{\color{orange}color individual \color{lightgreen} words in the middle }}$ of a sentence.
```
  


---
---
---
---



## Following works in most IDE's, but not on GitHub::

${\mathbf{\color{orange}Example \space Text}}$

${\mathrm{\color{orange}Example \space Text}}$

${\mathsf{\color{orange}Example \space Text}}$

${\mathtt{\color{orange}Examsple \space Text}}$

${\mathit{\color{orange}Example \space Text}}$

${\mathbb{\color{orange}Example \space Text}}$

${\mathcal{\color{orange}Example \space Text}}$

${\mathfrak{\color{orange}Example \space Text}}$





