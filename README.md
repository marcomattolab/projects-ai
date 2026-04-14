# AI Tool Demo & Exercises 🤖

A collection of AI tool demonstrations and hands-on exercises exploring modern AI technologies and protocols.

## 📁 Projects

### `010-mcp-server/` - Model Context Protocol Server
Learn the Model Context Protocol (MCP) with a practical server implementation featuring tools, prompts, and resources.

**Quick Start:**
```bash
cd 010-mcp-server
mcp dev main.py              # Development mode with inspector
mcp run main.py --transport=streamable-http  # Direct execution
```

**Features:**
- 🔧 Tools (greeting, text processing)
- 💬 Social media post prompts (Facebook, Twitter, LinkedIn, Medium, Personal Website)
- 📚 File-based resources (guidelines, templates)

## 🚀 Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install mcp fastmcp
```

## 📚 Learn More

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Python SDK](https://py.sdk.modelcontextprotocol.io/)
- [Official MCP Servers](https://github.com/modelcontextprotocol/servers)
