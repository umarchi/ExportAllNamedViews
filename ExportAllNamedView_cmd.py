import rhinoscriptsyntax as rs

__commandname__ = "ExportAllNamedView"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    
  # Get all layer names from recentfile
  allLayers = rs.LayerNames()
  num_layer = len(allLayers)
  
  # you can optionally return a value from this function
  # to signify command result. Return values that make
  # sense are
  #   0 == success
  #   1 == cancel
  # If this function does not return a value, success is assumed
  return 0
