# Implementação-TLB

Este código simula o funcionamento de uma memória cache, com o preenchimento da tabela de endereços e contagem de HIT e MISS dos acessos à memória. Além disso, apresenta algumas possibilidades de paridade para tratamento de SEU (single event upset) e MCU (multiple cell upset).

<h2> Configurações da TLB </h2>

- Cache de mapeamento associativo
- Cache com 8 posições
- Algoritmo de substituição: LRU
- Códificação da CAM da TLB: Paridade Simples, Paridade no MSB, Paridade dos bits pares no MSB e paridade dos bits ímpares no MSB-1
- Inserção de estatística de falhas na memória

<h2> Alunos </h2>

- Milena Maia
- Walber Florêncio

<h2> Orientador </h2>

- Otávio Alcântara

<h2> Laboratório de Sistemas Digitais </h2>

<img src="https://user-images.githubusercontent.com/59696629/152603654-3782f0eb-5937-40bd-955f-2206bd25dcab.png" width="250">

<h2> Desenvolvimento </h2>

- [x] Preenchimento dos endereços
- [x] Algoritmo de substituição
- [x] Contagem de HIT e MISS
- [x] Tratamento de Falsos Positivos
- [x] Mecanismo de injeção de falhas
- [x] Teste com código de correção de erros
  - [x] Paridade simples
  - [x] MSB
  - [x] MSB-1
  - [x] Proposta
- [x] Teste com aplicação real
  - [x] cc1 (testagem)
  - [x] Benchmark (experimentos finais)

<h2> Informação adicional </h2>

Código adaptado de Anselmo Battisti.

Adicionados scripts de teste já configurados
