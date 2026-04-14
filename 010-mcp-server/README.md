
✅ What is MCP?

MCP is the Model Context Protocol, a standardized way to expose tools, prompts, and resources from a server so clients can consume them in a consistent manner.

Useful links:
- https://py.sdk.modelcontextprotocol.io/
- https://modelcontextprotocol.io/docs/learn/client-concepts

Usefull video:
- https://www.youtube.com/watch?v=n7mhSdlz-Gw

Other MCP server:
- https://github.com/modelcontextprotocol/servers

Usage:
- `mcp dev main.py` - start the server in development mode and open the MCP Inspector for interactive testing.
- `mcp run main.py --transport=streamable-http` - run the server directly with a streamable HTTP transport.

What this project contains:
- `main.py` defines a simple MCP server with a greeting tool and a social media post prompt.
- The server exposes both tools and prompts via MCP, so clients can call them using the MCP protocol.

How it works:
- `mcp dev` loads `main.py`, starts the server, and provides a debugging/development experience.
- `mcp run` starts the server normally and uses the transport configured on the command line.

Tip:
- If you want to make changes to the server, update `main.py` and restart the MCP command.
