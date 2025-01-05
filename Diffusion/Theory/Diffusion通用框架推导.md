flow matching , score matching,  ddim/ddpm 都有一个统一的微分方程的框架。 

## SDE


$$
dx_t = f(x_t,t) + g(t) dw , dw = \sqrt{dt}\epsilon
$$
用线性近似$x_t$改写成：
$$
x_t = x_{t-\Delta t} + () \Delta t + () \Delta w
$$
其中$\Delta w =\sqrt{\Delta t} \epsilon$是一个维纳过程。 

DDPM加噪音公式：
$$
x_t = \sqrt{1-\beta_{t}} x_{t-1} + \sqrt{\beta_{t-1} }\epsilon
$$

改写成微分方程形式：
$$
x(t) =  \sqrt{1-\beta(t)}  x({t-1}) + \sqrt{\beta({t-1}) }\epsilon
$$

由泰勒公式得$\sqrt{1-x}$在x=0的地方展开，有$\sqrt{1-x}=1-\frac{1}{2}x +o()$，从而$\sqrt{1-\beta(t)}  =1-\frac{1}{2}\beta(t) +o()$带入上式可得：

$$
x(t) = (1-\frac{1}{2}\beta(t) ) x({t-1}) + \sqrt{\beta({t-1}) }\epsilon
$$
先凑一个$\Delta w$:
$$
x(t) = (1-\frac{1}{2}\beta(t) ) x({t-1}) + \sqrt{\frac{\beta({t-1)}}{\Delta t} } \sqrt{\Delta t}\epsilon
$$
再展开右边第一项:
$$
x(t) = x(t-1)-   \frac{1}{2}\beta(t)x({t-1})   + \sqrt{\frac{\beta({t-1)}}{\Delta t} } \sqrt{\Delta t}\epsilon
$$
然后凑一个$\Delta t$
$$
x(t) = x(t-1)-   \frac{1}{2} \frac{\beta(t)}{\Delta t} x({t-1})\Delta t   + \sqrt{\frac{\beta({t-1)}}{\Delta t} } \sqrt{\Delta t}\epsilon
$$
最后令$\frac{\beta(t)}{\Delta t} =\overline \beta(t)$
$$
x(t) = x(t-1)-   \frac{1}{2} \overline \beta(t) x({t-1})\Delta t   + \sqrt{\overline \beta(t)} {\Delta w}
$$
还要把时间步1改写成$\Delta t$
$$
x(t) = x(t-\Delta t)-   \frac{1}{2} \overline \beta(t) x({t-1})\Delta t   + \sqrt{\overline \beta(t)} {\Delta w}
$$
然后移项改写为微分方程
$$
x(t)-x(t-\Delta t) = -\frac{1}{2} \overline \beta(t) x({t-\Delta t})\Delta t   + \sqrt{\overline \beta(t)} {\Delta w}
$$
$$
dx(t) = -\frac{1}{2} \overline \beta(t) x({t})d t   + \sqrt{\overline \beta(t)} {\Delta w}
$$
其中 $f(x(t),t) = -\frac{1}{2} \overline \beta(t) x({t})$,$g(t) =  \sqrt{\overline \beta(t)}$
