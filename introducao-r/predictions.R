library(tidyverse)
library(modelr)

mpg %>%
  ggplot(aes(displ, hwy)) +
  geom_point()

# y = mx + b
#hwy ~ w * displ + b
model <- lm(hwy ~ displ, data = mpg)

pred <- predict(model, mpg)

mpg %>%
  add_predictions(model) %>%
  ggplot() +
  geom_point(
    aes(displ, hwy)
  ) +
  geom_point(
    aes(displ, pred),
    color = "red"
  )

mpg %>%
  add_residuals(model) %>%
  ggplot(aes(displ, resid)) +
  geom_point()

# y = mx + b
#hwy ~ w1 * displ + w2 * cy; + b
# Modelos lineares
model <- lm(hwy ~ displ + cyl + drv, data = mpg)
model

# Modelos Não lineares
model <- lm(hwy ~ displ * cyl, data = mpg)
model

mpg$drv

# Para acessar o help utiliza-se o caractere de interrogacao (?)
?mpg

