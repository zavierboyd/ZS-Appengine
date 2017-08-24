try:
    import matplotlib.pyplot as plt
    import mpld3 as mpl
except:
    pass
import numpy as np


def graph(data, x, y):
    try:
        x = np.array(data[x])
        xtest = sum(x.imag ** 2)
        fig = plt.figure()
        if y is None:
            if xtest != 0:
                y = x.imag
                x = x.real
            else:
                y = x
                x = range(len(x))
        else:
            y = np.array(data[y])
            ytest = sum(y.imag**2)
            x = abs(x) if xtest != 0 else x
            y = abs(y) if ytest != 0 else y
        plt.plot(x, y)
        return mpl.fig_to_html(fig)
    except:
        return placeholder


placeholder = ''' <style>

</style>

<div id="fig_el811644378604322271759321"></div>
<script>
function mpld3_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded){
   // already loaded: just create the figure
   !function(mpld3){

       mpld3.draw_figure("fig_el811644378604322271759321", {"axes": [{"xlim": [20.5, 31.5], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [20.5, 31.5], "ylim": [20.5, 31.5], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 10.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 10.0, "position": "left", "nticks": 7, "tickvalues": null}], "lines": [{"color": "#1F77B4", "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 2, "alpha": 1, "xindex": 0, "linewidth": 1.5, "data": "data01", "id": "el81164659969872"}], "markers": [], "id": "el81164601557904", "ydomain": [20.5, 31.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.10999999999999999, 0.775, 0.77]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[21.0, 21.0], [22.0, 22.0], [23.0, 23.0], [24.0, 24.0], [25.0, 25.0], [26.0, 26.0], [27.0, 27.0], [28.0, 28.0], [29.0, 29.0], [30.0, 30.0], [31.0, 31.0]]}, "id": "el81164437860432"});
   }(mpld3);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/mpld3
   require.config({paths: {d3: "https://mpld3.github.io/js/d3.v3.min"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){

         mpld3.draw_figure("fig_el811644378604322271759321", {"axes": [{"xlim": [20.5, 31.5], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [20.5, 31.5], "ylim": [20.5, 31.5], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 10.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 10.0, "position": "left", "nticks": 7, "tickvalues": null}], "lines": [{"color": "#1F77B4", "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 2, "alpha": 1, "xindex": 0, "linewidth": 1.5, "data": "data01", "id": "el81164659969872"}], "markers": [], "id": "el81164601557904", "ydomain": [20.5, 31.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.10999999999999999, 0.775, 0.77]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[21.0, 21.0], [22.0, 22.0], [23.0, 23.0], [24.0, 24.0], [25.0, 25.0], [26.0, 26.0], [27.0, 27.0], [28.0, 28.0], [29.0, 29.0], [30.0, 30.0], [31.0, 31.0]]}, "id": "el81164437860432"});
      });
    });
}else{
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://mpld3.github.io/js/d3.v3.min.js", function(){
         mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.2.js", function(){

                 mpld3.draw_figure("fig_el811644378604322271759321", {"axes": [{"xlim": [20.5, 31.5], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [20.5, 31.5], "ylim": [20.5, 31.5], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 10.0, "position": "bottom", "nticks": 7, "tickvalues": null}, {"scale": "linear", "tickformat": null, "grid": {"gridOn": false}, "fontsize": 10.0, "position": "left", "nticks": 7, "tickvalues": null}], "lines": [{"color": "#1F77B4", "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 2, "alpha": 1, "xindex": 0, "linewidth": 1.5, "data": "data01", "id": "el81164659969872"}], "markers": [], "id": "el81164601557904", "ydomain": [20.5, 31.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.10999999999999999, 0.775, 0.77]}], "height": 480.0, "width": 640.0, "plugins": [{"type": "reset"}, {"enabled": false, "button": true, "type": "zoom"}, {"enabled": false, "button": true, "type": "boxzoom"}], "data": {"data01": [[21.0, 21.0], [22.0, 22.0], [23.0, 23.0], [24.0, 24.0], [25.0, 25.0], [26.0, 26.0], [27.0, 27.0], [28.0, 28.0], [29.0, 29.0], [30.0, 30.0], [31.0, 31.0]]}, "id": "el81164437860432"});
            })
         });
}
</script>'''

if __name__ == '__main__':
    data = {'x': [i-(i*1j) for i in range(10)], 'y': range(10)}
    x = sum(np.array(data['x']).imag**2)
    print(x.imag, x.real)
    with open('graph.html', 'w') as f:
        f.write(graph(data, 'x', 'y'))

    # y = graph(data, 'x', 'y')
