
## Introduction of Finite Automata

  __Finite Automata(FA)__ is the simplest machine to recognize patterns.
The finite automata or finite state machine is an abstract machine that has five elements or tuples.
It has a set of states and rules for moving from one state to another but it depends upon the applied input symbol.
Basically, it is an abstract model of a digital computer.
The following figure shows some essential features of general automation.

![fanite automata](/assets/automata-300x240.png "Features of Finite Automata")

_Figure: Features of Finite Automata_

> The above figure shows the following features of automata:

1. Input
2. Output
3. States of automata
4. State relation
5. Output relation

> A Finite Automata consists of the following :

`Q : Finite set of states`<br />
`Σ : set of Input Symbols`<br />
`q : Initial state`<br />
`F : set of Final States`<br />
`δ : Transition Function`<br />

> Formal specification of machine is

`{ Q, Σ, q, F, δ }`

> FA is characterized into two types:

1 Deterministic Finite Automata (DFA) –

`DFA consists of 5 tuples {Q, Σ, q, F, δ}.`<br />
`Q : set of all states.`<br />
`Σ : set of input symbols. ( Symbols which machine takes as input )`<br />
`q : Initial state. ( Starting state of a machine )`<br />
`F : set of final state.`<br />
`δ : Transition Function, defined as δ : Q X Σ --> Q.`<br />

In a DFA, for a particular input character, the machine goes to one state only. A transition function is defined on every state for every input symbol. Also in DFA null (or ε) move is not allowed, i.e., DFA cannot change state without any input character.

For example, below DFA with `Σ = {0, 1}` accepts all strings ending with 0.

![DFA with  Σ = {0, 1} ](/assets/Finite_automata_introduction_1.jpg "DFA with  Σ = {0, 1} ")

_Figure: DFA with  Σ = {0, 1}_

One important thing to note is, __there can be many possible DFAs for a pattern.__ A DFA with a minimum number of states is generally preferred.

2 Nondeterministic Finite Automata(NFA)
NFA is similar to DFA except following additional features:

1. Null (or ε) move is allowed i.e., it can move forward without reading symbols.
2. Ability to transmit to any number of states for a particular input.

However, these above features don’t add any power to NFA. If we compare both in terms of power, both are equivalent.

Due to the above additional features, NFA has a different transition function, the rest is the same as DFA.

`δ: Transition Function`<br/>
`δ:  Q X (Σ U ε ) --> 2 ^ Q.`

As you can see in the transition function is for any input including null (or ε), NFA can go to any state number of states.
For example, below is an NFA for the above problem.

![NFA](/assets/Finite_automata_introduction_2.jpg "NFA")

_NFA_

One important thing to note is, ___in NFA, if any path for an input string leads to a final state, then the input string is accepted. For example, in the above NFA, there are multiple paths for the input string “00”. Since one of the paths leads to a final state, “00” is accepted___ by the above NFA. 

###### Some Important Points:
- Justification: 

Since all the tuples in DFA and NFA are the same except for one of the tuples, which is Transition Function (δ) 

In case of DFA
`δ : Q X Σ --> Q`<br/>
In case of NFA
`δ : Q X Σ --> 2Q`

Now if you observe you’ll find out Q X Σ –> Q is part of Q X Σ –> 2Q.


On the RHS side, Q is the subset of 2Q which indicates Q is contained in 2Q or Q is a part of 2Q, however, the reverse isn’t true. So mathematically, we can conclude that __every DFA is NFA but not vice-versa.__ Yet there is a way to convert an NFA to DFA, so __there exists an equivalent DFA for every NFA.__ 

1. Both NFA and DFA have the same power and each NFA can be translated into a DFA. 
2. There can be multiple final states in both DFA and NFA. 
3. NFA is more of a theoretical concept. 
4. DFA is used in Lexical Analysis in Compiler. 
