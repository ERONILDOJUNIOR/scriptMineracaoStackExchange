# Assertion Roulette

## 🔍 Descrição do Problema

**Assertion Roulette** ocorre quando um método de teste em Dart contém múltiplas **expectativas** (`expect`) sem uma mensagem descritiva ou contexto adequado. Isso torna difícil identificar qual expectativa falhou e por quê, prejudicando a legibilidade e a manutenção do teste.

Em outras palavras, o **Assertion Roulette** ocorre quando o teste "joga a roleta" com o desenvolvedor, deixando-o adivinhar qual expectativa falhou.

-----

## ⚠️ Sintomas e Impacto

  * **Dificuldade de Depuração**: Quando uma expectativa falha, o motivo exato não fica claro, especialmente se mais de duas expectativas estão presentes.
  * **Redução da Manutenção**: Esse problema pode dificultar o trabalho de outros desenvolvedores ao tentar entender o teste, aumentando o custo de manutenção.
  * **Baixa Legibilidade**: O código se torna confuso, dificultando a identificação das condições testadas.

-----

## 🔑 Critérios de Identificação

Para identificar o **Assertion Roulette**, procure por:

  * Métodos de teste que contenham múltiplas **expectativas** (`expect`) sem mensagens descritivas.
  * Testes os quais não especificam claramente qual a condição testada em questão.

-----

## ✅ Exemplo de Código

### Exemplo com Assertion Roulette

```dart
import 'package:flutter_test/flutter_test.dart'; // Ou 'package:test/test.dart;' para testes de unidade sem Flutter

void main() {
  test('Teste com Assertion Roulette', () {
    final valores = [10, 20, 30];

    expect(valores.length, 4); // Falha possível, mas sem indicar o motivo
    expect(valores[0], 5); // Outra falha possível, sem explicação
    expect(valores.contains(50), true); // Falha possível, sem contexto
  });
}
```

### Exemplo sem Assertion Roulette

```dart
import 'package:flutter_test/flutter_test.dart'; // Ou 'package:test/test.dart;' para testes de unidade sem Flutter

void main() {
  test('Teste sem Assertion Roulette', () {
    final valores = [10, 20, 30];

    expect(valores.length, 4, reason: "A lista deve conter exatamente 4 elementos");
    expect(valores[0], 5, reason: "O primeiro valor da lista deveria ser 5");
    expect(valores.contains(50), true, reason: "A lista deveria conter o valor 50");
  });
}
```

-----

## 🚀 Correções Sugeridas

Para resolver o Assertion Roulette:

  * **Adicione Mensagens de Descrição**: Inclua mensagens para cada **expectativa** usando o parâmetro `reason`, explicando a condição esperada e o motivo da verificação.
  * **Reduza a Quantidade de Expectativas**: Se possível, divida o teste em testes menores, o que melhora a clareza e torna o código mais modular.
  * **Utilize Mocks e Verificações Explícitas**: Em casos mais complexos, considere usar um framework de mock (como `mockito`) para isolar unidades de código e verificar interações com dependências, permitindo que você crie **expectativas** mais focadas.

-----

## 🌟 Exceções e Casos Especiais

Em testes simples ou triviais com uma única **expectativa**, pode ser aceitável omitir uma mensagem de contexto. Contudo, para qualquer teste com múltiplas verificações, adicionar descrições é recomendado.

-----

## 🛠 Ferramentas de Detecção

  * **Linter Configurável**: Ferramentas como `dart analyze` podem ser configuradas com regras personalizadas para identificar métodos de teste com múltiplas expectativas sem o parâmetro `reason`.
  * **Plugins para Test Smells**: Ferramentas de análise de código estática como **SonarQube** podem ser estendidas com regras personalizadas para Dart para monitorar múltiplas expectativas sem descrições explícitas.

-----

## 📝 Nota

O Assertion Roulette é especialmente relevante em projetos complexos onde múltiplas condições são verificadas em cada teste. Este guia ajuda a garantir que cada falha seja clara e fácil de rastrear, melhorando a qualidade e a manutenibilidade do seu código Dart.

-----

## 📚 Referências e Estudos Relacionados

  * Fowler, M. (1999). *Refactoring: Improving the Design of Existing Code*
  * Meszaros, G. (2007). *xUnit Test Patterns: Refactoring Test Code*
