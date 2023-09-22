# Função que calcula a composição de duas funções 

def composicao(f, g, x): 

    return f(g(x)) 

  

# Funções f(x) e g(x) fornecidas como entrada 

def f(x): 

    return x**2 

  

def g(x): 

    return x - 1 

  

# Exemplos de cálculo das composições 

x = 4 

  

gof = composicao(g, f, x) 

gog = composicao(g, g, x) 

fof = composicao(f, f, x) 

fog = composicao(f, g, x) 

  

# Imprime os resultados 

print("(g ∘ f)(4) =", gof) 

print("(g ∘ g)(4) =", gog) 

print("(f ∘ f)(4) =", fof) 

print("(f ∘ g)(4) =", fog) 