from mcp.server.fastmcp import FastMCP

# Create an MCP Server
mcp = FastMCP("MCP Marcomatto", json_response=True)

# Add a simple tool for demonstration
@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"

# Add a prompt for demonstration that receive a title and a description about a post 
# a social hub like facebook, twitter, linkedin, Medium, personalWebsite and 
# return a post ready to be published in the social hub based on a specific prompt
@mcp.prompt()
def create_social_media_post(title: str, description: str, social_hub: str) -> str:
    """Create a social media post based on the title, description and social hub"""
    if social_hub.lower() == "facebook":
        return f"Facebook Post: {title}\n{description}\n#Facebook"
    elif social_hub.lower() == "twitter":
        return f"Twitter Post: {title}\n{description}\n#Twitter"
    elif social_hub.lower() == "linkedin":
        return f"LinkedIn Post: {title}\n{description}\n#LinkedIn"
    elif social_hub.lower() == "medium":
        return f"Medium Post: {title}\n{description}\n#Medium"
    elif social_hub.lower() == "personalwebsite":
        return f"Personal Website Post: {title}\n{description}\n#PersonalWebsite"
    else:
        return "Unsupported social hub. Please choose Facebook, Twitter, LinkedIn, Medium, or Personal Website."
    
# Add a resource for demonstration that receive name of a resource (which is a file name) 
# and return content of the resource (file content) based on the name of the resource
@mcp.resource("file://documents/{resource_name}")
def get_resource(resource_name: str) -> str:
    """Get the content of a resource based on its name"""
    if resource_name == 'guideline':
        file_path = 'guideline.txt'  
    elif resource_name == 'template':
        file_path = 'template.txt'  
    else:
        return f"Resource '{resource_name}' is not recognized. Available resources: guideline, template."
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Resource '{file_path}' not found."
    