## Writing Markdown Code

Markdown is a lightweight markup language for creating formatted text using a plain-text editor. Here are some basics:

#### Headers
```markdown
# H1
## H2
### H3
#### H4
##### H5
###### H6
```

#### Emphasis
```markdown
*Italic* or _Italic_
**Bold** or __Bold__
~~Strikethrough~~
```

#### Lists
**Unordered List**:
```markdown
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2
```

**Ordered List**:
```markdown
1. Item 1
2. Item 2
   1. Subitem 1
   2. Subitem 2
```

#### Links
```markdown
[OpenAI](https://www.openai.com)
```

#### Images
```markdown
![Alt text](url)
```

#### Code
**Inline Code**:
```markdown
Here is some `inline code`.
```

**Code Block**:
```markdown
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
```

### Example Markdown File

Create `docs/README.md` and add the following content:

```markdown
# Project Title

## Introduction

This project is an example for learning Git and GitHub.

## Directory Structure

- \`docs/\`: Documentation files.

## Usage

To clone this repository, run:

\`\`\`bash
git clone https://github.com/yourusername/my-project.git
\`\`\`

## License

This project is licensed under the MIT License.
```