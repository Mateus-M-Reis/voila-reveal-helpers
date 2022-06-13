# Voila Presentation Templates

These are utility tools to style your cells to be rendered with [voila]() using the reveal template.  

## What does it do

The code in this module is contained in two files: [html_templates]() e [slides_templates]().  
From the first one you can import a function that returns a template for the title slide of your presentation:

```python
from templates.html_templates import return_title_slide

return_title_slide(
    'Title of Your Presentation. <br>A long title', 
    'Your name, ...'
)
```

![](/home/mop/Códigos/voila-reveal-helpers/assets/Screenshot%20from%202022-06-12%2021-31-21.png)

as well for index slides:

```python
from templates.html_templates import return_index_slide

return_index_slide(
    'Introduction',
    """<ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>"""
```

![](/home/mop/Códigos/voila-reveal-helpers/assets/Screenshot%20from%202022-06-12%2021-33-30.png)

From the [slides_templates]() file the are utilities to build slides with tree different layouts for now.  
The first template is that of a slide with one title and one content:

```python
import numpy as np
import pandas as pd
import bqplot.pyplot as plt

from templates.slides_templates import return_slide_1

df = pd.DataFrame(np.random.randn(10,4).cumsum(0),
                 columns=['A','B','C','D'],
                 index=np.arange(0,100,10))
fig = plt.figure()
plt.plot(df.T)

return_slide_1('One Content Slide', fig)
```

![](/home/mop/Códigos/voila-reveal-helpers/assets/Screenshot%20from%202022-06-12%2021-52-55.png)

You can also build a slide with two columns:

```python
from templates.slides_templates import return_slide_11

return_slide_11(
    'Two Columns Slide', 
    """<h2>Right Column HTML content</h2>
    <p>bla bla bla</p>
    $$E=mc^2$$
    """, 
    fig
)
```

![](/home/mop/Códigos/voila-reveal-helpers/assets/Screenshot%20from%202022-06-12%2021-34-59.png)
