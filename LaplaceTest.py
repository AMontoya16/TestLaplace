from manim import *
import math

class LaplaceTransformScene(Scene):
    def construct(self):
        # 1. Introducción
        title = Text("Laplace Transform", font_size=48)
        notation = MathTex(r"X(s) = \mathcal{L}\{x(t)\}", font_size=48)
        definition = MathTex(r"X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} dt", font_size=48)
        variable = MathTex(r"s = \sigma + j\omega")

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition))
        self.wait(1)
        self.play(Transform(definition,notation))
        self.wait(1)
        self.play(FadeOut(notation,definition))
        self.play(Write(variable))
        self.wait(2)

        # 2. Ejemplo
        example_title = Text("Example", font_size=48)
        self.play(FadeOut(title, variable))
        self.play(Write(example_title))
        self.wait(1)
        self.play(example_title.animate.to_edge(UP))

        hs_orig = MathTex(r"H(s) = \frac{s}{s^2 + 2s + 4}", font_size=48)
        hs_estable = MathTex(r"\text{Note: } H(s) \text{ is stable}", font_size=40)
        self.play(Write(hs_orig))
        self.play(Write(hs_estable.next_to(hs_orig, DOWN)))
        self.wait(2)
        self.play(FadeOut(hs_estable))

        hs_factored = MathTex(
            r"H(s) = \frac{s}{(s - (-1 + j\sqrt{3}))(s - (-1 - j\sqrt{3}))}",
            font_size=48
        )
        self.play(Transform(hs_orig, hs_factored))
        self.wait(1)

        # Polos y cero texto
        poles_text = MathTex(r"\text{Poles: } s = -1 \pm j\sqrt{3}", font_size=40)
        zero_text = MathTex(r"\text{Zero: } s = 0", font_size=40)

        self.play(Write(poles_text.next_to(hs_factored, DOWN)))
        self.play(Write(zero_text.next_to(poles_text, DOWN)))
        self.wait(2)
        self.play(FadeOut(hs_factored, poles_text, zero_text, example_title, hs_orig))


        # Crear plano sin etiquetas automáticas
        axes = NumberPlane(
            x_range=[-6, 4],
            y_range=[-4, 4],
            background_line_style={"stroke_opacity": 0.3},
            y_axis_config={"include_ticks": True},
            x_axis_config={
                "include_ticks": True,
                "include_numbers": True
            }
        )

        axes_label = Text("Zeros and poles diagram of H(s)", font_size=28).to_corner(UL)

        # Etiquetas personalizadas del eje y solo con j
        y_labels = {
            -3: MathTex(r"-3j", font_size=28),
            -2: MathTex(r"-2j", font_size=28),
            -1: MathTex(r"-j", font_size=28),
             0: MathTex(r"0", font_size=28),
             1: MathTex(r"j", font_size=28),
             2: MathTex(r"2j", font_size=28),
             3: MathTex(r"3j", font_size=28)
        }
        for y_val, label in y_labels.items():
            label.next_to(axes.c2p(0, y_val), LEFT, buff=0.15)
            self.add(label)

        # Ejes σ y jω
        sigma_label = MathTex(r"\sigma", font_size=28).next_to(axes.x_axis, RIGHT)
        jw_label = MathTex(r"j\omega", font_size=28).move_to(axes.c2p(0.3,3.6))  # arriba derecha

        self.play(Create(axes), FadeIn(axes_label), FadeIn(sigma_label), FadeIn(jw_label))
        self.wait(1)

        # Polos y cero
        pole1 = complex(-1, math.sqrt(3))
        pole2 = complex(-1, -math.sqrt(3))
        zero = complex(0, 0)

        cross1 = Cross(Dot(axes.c2p(pole1.real, pole1.imag), radius=0.12), color=RED)
        cross2 = Cross(Dot(axes.c2p(pole2.real, pole2.imag), radius=0.12), color=RED)
        zero_dot = Dot(axes.c2p(zero.real, zero.imag), color=GREEN, radius=0.12)

        self.play(FadeIn(cross1), FadeIn(cross2), FadeIn(zero_dot))
        self.wait(1.5)

        # ROC: Re(s) > -1
        roc_rect = Rectangle(
            width=8,
            height=8,
            color=BLUE,
            fill_opacity=0.2,
            stroke_opacity=0
        ).align_to(axes.c2p(-1, 0), LEFT)

        roc_label = MathTex(r"\text{ROC: } Re(s) > -1", font_size=30).next_to(axes_label, DOWN)
        roc_label2 = MathTex(r"\text{ROC: } \sigma > -1", font_size=30).next_to(axes_label, DOWN)
        self.play(FadeIn(roc_rect), FadeIn(roc_label))
        self.wait(1)
        self.play(Transform(roc_label,roc_label2))
        self.wait(2)