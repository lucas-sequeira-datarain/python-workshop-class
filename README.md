# Python Workshop

**Lucas Nunes Sequeira: AWS** - *07/10/2022*

---

### Acesse este workshop em:

<img src="assets/qr_code.png" width="300px">

---

### 1. Intro

Python é uma linguagem de programação orientada a objetos.

Quase tudo em Python é um objeto, com suas propriedades e métodos.

Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.

---

### 2. Definindo uma Classe

Para definir uma classe, usamos a palavra-chave `class`:

```python
class MyClass:
    x = 5
```

---

### 3. Criando Objetos

Para criar objetos, usamos o nome da classe, seguido de parênteses:

```python
p1 = MyClass()
```

---

### 4. O Método `__init__()`

O método `__init__()` é um método especial (método dunder/mágico), chamado sempre que a classe é usada para criar um novo objeto. Importante para inicializar os atributos do objeto, por exemplo.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### 5. A variável `self`

A variável `self` é uma referência à instância atual da classe, e é usada para acessar variáveis que pertencem à classe. Assim, para acessar variáveis da instância (de dentro da mesma), usamos `self`. Para acessar variáveis da classe (de fora da classe), usamos a própria variável do objeto da classe criada para acessar as variáveis/métodos da classe.

```python
p1 = Person("Lucas", 25)
print(p1.name)
print(p1.age)

>> Lucas
>> 25
```

---

### 6. Métodos

Métodos em classes funcionam da mesma forma que funções, mas são definidos dentro da classe.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
```

Podemos acessar os métodos da classe internamente com `self`, e externamente com o nome do objeto da classe.

```python
p1 = Person("Lucas", 25)
p1.myfunc()

>> Hello my name is Lucas
```

### 7. Herança

Herança é uma forma de criar uma nova classe, que herda todos os métodos e propriedades de uma classe existente.

```python
class Collaborator(Person):
    def __init__(self, name, age, area):
        super().__init__(name, age)
        self.area = area   

c1 = Collaborator("Lucas", 25, "Dev")
c1.myfunc()

>> Hello my name is Lucas
```

Neste exemplo, a classe `Collaborator` herda todos os métodos e propriedades da classe `Person`, e adiciona o atributo `area`. Observe que neste caso, utilizamos o método `super()` para chamar o método `__init__()` da classe pai, para que a classe filho possa inicializar os atributos da classe pai.

Além disso, como mencionado esta nova classe, herda todos os métodos da classe pai, podemos sobrescrever os métodos da classe pai, caso necessário.

```python
class Collaborator(Person):
    def __init__(self, name, age, area):
        super().__init__(name, age)
        self.area = area

    def myfunc(self):
        print("Hello my name is " + self.name + " and I work in " + self.area)

c1 = Collaborator("Lucas", 25, "Dev")
c1.myfunc()

>> Hello my name is Lucas and I work in Dev
```

### 8. Encapsulamento

Encapsulamento é o conceito de esconder detalhes de implementação e mostrar apenas o necessário para o usuário. Em Python, não existe o conceito de encapsulamento, mas podemos usar convenções para indicar que um método ou atributo não deve ser acessado diretamente.

```python
class MyClass:
    def __init__(self):
        self.__hiddenVariable = 0

    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

p = MyClass()
print(p.__hiddenVariable)

>> AttributeError: 'MyClass' object has no attribute '__hiddenVariable'

print(p._MyClass__hiddenVariable)

>> 0
```

### Algumas Referências

- [W3 Schools - Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- [AWS - Python Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/variables)
- [Arjan Codes - Python Development](https://www.youtube.com/c/ArjanCodes)
