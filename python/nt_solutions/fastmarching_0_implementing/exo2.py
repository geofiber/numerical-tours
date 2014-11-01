"""
Implement the Fast Marching algorithm.
Display from time to time the front that propagates.
"""
options.method = 'fm'
options.svg_rate = n*6
[D, Dsvg, Ssvg] = perform_dijkstra_fm(W, x0, options)
for i in arange(0,4):
    subplot(2, 2, i)
    d = Dsvg[:,:,2+i]
    d[d==Inf] = 0
    imageplot(d)
    colormap(jet(256))