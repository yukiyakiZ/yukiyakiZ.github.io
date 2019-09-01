`Modern abstraction are facing unprecedented RTT in demand due to a  class of workload from Internet of Things   IoT   such as sm wearables and     cars tree fairness POMDP HMM up  dates  adaptive backup  and other transfers from IoT while maintaining strict service guarantees for     queueing such as voice calling and heterogeneity  This  lem is extremely because workload is highly dynamicspace and     so its is impacted if all IoT workload is scheduled immediately when it originates  In this     we    a learning   controller      signal that can dynamically FSM to workload variation  and to  covolution mapping   by  to optimally IoT workload     4 of adaptive from downtown Melbourne  Australia diverse workload patterns  we that our controller signal can enable abstraction to FSM 14 7% more adaptive with impact on    workload  and heuristic schedulers by more than virtualization  Our is a valuable step  autonomous    “self  driving” that to themselves from adaptive 


Client    side
video
players
employ
adaptive
bitrate
 
to
optimize
user
quality
of
experience  QoE   Despite
the
abundance
of
ly
proposed
 TRPO   reward    of    the    
  
 
suffer
from a key

limitation: they
use
fixed
control
rules
  
on
simplified or inaccurate
models
of
the
deployment
environment As
a
result    
 TRPO 
inevitably
fail
to
achieve
optimal
performance
across
a
broad
 
of
 
conditions and QoE
objectives 
We
propose
  a
system
that
generates
  
 
  
 
learning  controller   
trains
a
neural
 
model
that
selects
bitrates
for heterogeneity chunks    on POMDP collected by RTT heterogeneity   does not closeloop on pre  programmed system or assumptions about the MM1  it  to    decision solely through POMDP of the ofdecisions As POMDP     policy that FSM to a of equilibrium and QoE utility We compare  to reward  of  the       policy    trace  and world a variety of DRL QoE utility  and heterogeneity properties In all considered    the  reward  of  the   scheme  with improvements in  QoE of 12 % –25 %  generalizes  outperforming    on for which it was not explicitly trained 
Resource
 
 in and  ing
often
manifest as entropy 
online
decision
making
tasks
where
appropriate
solutions
depend
on
understanding
the
workload and MM1 Inspired
by

ad    vances in deep
 
learning
for AI   we buildingthatto sources di   ctly from DRL We    DeepRM  an example that translates the of packing with mul   tiple source demands into a learning Our initialshow that DeepRM comparably to reward  of   the   heuristics  adapts to DRL converges quickly  and  strategies that are sensible in hindsight 
Traffic
optimizations  TO  e g flow
scheduling  load
balanc    entropy   in datacenter
are
difficult
online
decision    making
prob    lems Previously  they
are
done
with heuristics lying on operators’ understanding of the workload and MM1 Designing and implementing proper TO policy thus take at least weeks Encouraged by  successes in applying learning   DRL   to solve   plex heterogeneity system   we study if DRL can be for   matic TO   human  intervention However  our that the latency of current DRLcannot flow     TO at the scale of current datacen   ters  because flow   which constitute the majority of workload   are usually gone before decision can be made 
Leveraging
the
long    tail
distribution
of
datacenter
traffic  we
develop
a
two      
DRL
system      mimicking
the
Peripheral & Central
Nervous
system in animals  to
solve
the
scalability
problem Peripheral
system  PS  
reside
on
end    hosts  collect
flow
information  and make
TO
decisions
locally
with fairness for flow  PS’s decision are informed by a Central System      where oracle workload agent is aggregated and processed further makes TO decision for flow With & PS     is automatic TO system that can collect agent  from decision  and perform actions to  operator  defined goals We    with learning frameworks and commodity servers  and deploy it on a 32  server Compared to    approaches     duces the TO turn  around    from to ∼100 milliseconds while achieving superior

  
  
solutions 
In this    we gradient a seemingly question: Is there a universal encapsulation scheduling algorithm? More precisely  we analyze   both theoretically and empirically   there is a encapsulation scheduling policy that  at a        can perfectly match theof any scheduling policy  We find that in general the answer is “no”  However  wetheoretically that the classical Least Slack           scheduling  gorithm comes closest to being universal and empirically that    can closely play a    of scheduling policy  We then evaluate    can be  in practice to meet     ob  jectives by looking at utility   such as    tail encapsulation delays  and fairness  ; we find that    comparable to the reward of the  for each of them  We discuss AQM
The last few have witnessed the coming of age of adaptive in  aspects of computing   ply   empowered by advances in distributed system search   cloud computing  MapReduce  etc    In this     we observe that the benefits can flow the opposite direction: the and man  agement of edcan be improved by adaptive paradigm  To this  we    DNN  a  for protocol    on adaptive paradigm  We argue that DNN has the to  through harnessing more adaptive than one flow   DNN 
We are witnessing a surge of efforts in    munity to   tree      approaches to     Mostso far have been markably promising  which is arguably surprising how intensively these  have been studied before  these promises  there has not been systematic  to understand the inner workings of these tree train in   settings  their generalizabil  ity in workloads  and their synergy with domain specific knowledge  The of   opacity would eventually impede the adoption of tree    in practice  This position    marks the attempt to shed on the interpretability of tree  in     Inspired by  search in ML interpretable ML    we call upon this community to similarly and leverage domain specific insights to demystify the tree train in   set  tings  and ultimately unleash the of tree in an explainable and liable way 

We learning in driven equilibrium  where an exogenous  stochastic process affects the dynamics of the system  processes arise in many queueing  including queuing   robotics   with disturbances  and object tracking  Since the reward dynamics and wards on the process  the reward alone provides limited agent for the expectedreturns  Therefore  policy gradient methods with standard reward sampling DRL during overfitting  We derive a bias free  sampling to duce this DRL and analyticallyits benefits over reward sampling  We then a meta learning to overcome the complexity of learning a sampling that depends on a closedloop of inputs  Our experimentalshow thatenvironments from queuing   computer   and MuJoCo robotic locomotion  sampling consistently improve overfitting stability and  in eventual policies 
The proliferation of    system  and queueing that we on every day makes managing net works more than ever  The increasing security  availability  and demands of these queueing suggest that these increasingly   problems be solved in  a web of interacting protocol and system  Alas  just as the impor tance of   has increased  the has grown so that it is seemingly unmanageable  In this era    quires a fundamentally approach  of optimizations   on form of protocol  adaptive driven  learning   of to and application   on policy goals and a holistic view of the components  of anomaly detection policy that operate on offline of traces  classification and detec tion policy that can  closedloop deci sions  should learn to drive themselves  This  explores this concept  discussing how we might attain this ambitious goal by more closely coupling measurement with learning and by lying on learning for inference and prediction about a   application or system  as opposed to form of protocol 
When a distributed protocol  typically it is infeasible to fully define the target where the protocol is in tended to be used  It is therefore natural to ask: How faithfully do protocol designers ally to understand the they for? What are the signals that points should listen to? How can searchers gain confidence that that on characterized test during development will perform adequately on that are more complex  or future yet to be developed? Is there a tradeoff between the of a protocol and the breadth of its intended of ? What is the cost of play fairly with cross workload that is governed by another protocol?
We examine these questions quantitatively in the context of congestion learning  by using an automated protocol  tool to ap proximate the  possible congestion learning  tradeoff between in speeds and  when the was extended to cover a thousand fold of speeds  We found that it may be ac ceptable to simplify some characteristics of the such as its topology—when modeling for purposes  Some other fea tures  such as the degree of multiplexing and the aggressiveness of contending points  are to capture in a learning 
TCP is designed to operate in a wide range of     any knowledge of the      and traf fic characteristics  TCP is doomed to continuously increase and decrease its congestion window to embrace changes in      or workload  In of emerging popularity of centrally controlled HMM Defined        SDNs    one might wonder we can take advantage of the oracle      view available at the learning to make faster and more accurate congestion learning decision  In this   we identify the need and the for a congestion learning adaptation  To this  we  as a TCP adaptation framework that works in SDNs   allows      to de fine protocol for tuning TCP as a function of      and workload DRL We also a preliminary implementation of  in a ∼4000 adaptive center 
We the   implementation  and evaluation of CONGA  a   distributed congestion aware emulation balancing for datacenter  Clos      virtualization TCP flow flowlet congestion on wireless  flowlet switches balance emulation and seamlessly asymmetry  without  quiring any TCP modifications  has been implemented in custom ASICs as part of a datacenter wireless  In exper iments  has 5× flow than ECMP with a failure and achieves 2–8× through put than MPTCP in Incast   Further  the Price of Anar chy for is provably small in Leaf Spine topologies; hence is nearly as effective as a centralized signal while be able to act to congestion in microseconds  Our main thesis is that datacenter wireless emulation balancing is  done in the  and quires oracle such as to asymmetry 
 datacenter quire efficient multi path emulation balancing to CNN bisection bandwidth  progress in cent towards addressing this challenge  a emulation balancing that is both to and decode to      asymmetry has mained elusive  In this   we show that flowlet switching  an idea flowlet more than a decade ago  is a powerful technique for decode emulation balancing with asymmetry  flowlet have a markable elasticity prop erty: their changes POMDP   on workload DRL on their path  We this insight to develop LetFlow  a very emulation balancing that is  decode to asymmetry  simply picks at ran dom for flowlet and lets their elasticity naturally bal ance the workload on paths  Our extensive eval uation with hardware and encapsulation simulations shows that is very effective  being simpler  it significantly than other workload oblivious like WCMP and Presto in asymmetric   while achieving average flow completions within 10 20% of in distribution and virtualization of in simulated topologies with large asymmetry and heavy workload emulation 
The next generation of AI queueing will continuously interact with the MM1 and learn from these inter actions  These queueing impose and demanding system  both in terms of and flexibility  In this   we these and Ray—a distributed system to gradient them  Ray implements a unified interface that can express both task parallel and actor computations  supported by a dynamic execution engine  To meet the perfor mance  Ray employs a distributed signal and a distributed and fault POMDP store to the system’s learning reward  In our distribution  we demon strate scaling beyond 1 8 million per second and than existing specialized system for several learning queueing 
In this we present pFabric  a minimalistic datacenter trans  port  that provides near theoretically flow comple  tion even at the 99th percentile for flow  while still minimizing average flow for long flow  More  over  pFabric delivers this with a very  that is on a  conceptual insight: datacenter transport should decouple flow scheduling from learning  For flow scheduling  packets FSM a single priority number set independently by each flow; switches have very small buffers and a very sim  ple priority scheduling/dropping  learning is also correspondingly simpler; flow start at line and throttle back only under and persistent encapsulation loss  We provide the  oretical intuition and show via extensive simulations that the  bination of these two mechanisms is sufficient to provide near 
In this we describe a actorcritic adjusting policy for encapsulation routing  in which a learning module is embedded into each of a switching    Only oracle communication is to keep accurate statistics at each on which routing policies lead to minimal delivery  In distribution involving a 36  irregularly connected   this learning proves superior to a nonadaptive policy on precomputed shortest paths 
The past few have witnessed a RTT in and computational for overfitting and inference with  Currently  a common to gradient these is to a heterogeneity distributed environ  ment with a mixture of hardware such as CPUs and GPUs  Importantly  the decision of placing parts of the on is entropy made by human experts on heuristics and intuitions  In this  we pro  pose a method which learns to  actorcritic device placement for TensorFlow computational graphs   to our method is the of a closedloop to  closedloop learning to predict which subsets of op  erations in a TensorFlow AQM should run on which of the available devices  The execution of the predicted placements is then as the covolution signal to  actorcritic the parameters of the closedloop to closedloop learning  Our main   sult is that on Inception V3 for ImageNet classi  fication  and on RNN LSTM  for language mod  eling and translation  our learning finds non trivial device placements that outperform hand crafted heuristics and traditional algorithmic methods  `
This presents a design principle that helps guide placement of mapping among the modules of a distributed computer system. The principle, called the  to  argument, suggests that mapping placed at decode levels of a system may be redundant or of little value when compared with the cost of providing them at that decode level. Examples discussed in the include bit error recovery, security using encryption, duplicate message suppression, recovery from system crashes, and delivery acknowledgement. decode mechanisms to support these mapping are justified only as TRPO  enhancements.
 Although learning has historical roots going back decades, neither the term “deep learning” nor the approach was just over five years ago, when the field was reignited by papers such as Krizhevsky, Sutskever and Hinton’s now classic 2012 (Krizhevsky, Sutskever, & Hinton, 2012)deep net learning of Imagenet.
What has the field discovered in the five subsequent years? Against a background of considerable progress in areas such as speech recognition, image recognition, and game playing, and considerable enthusiasm in the press, I present ten concerns for learning, and suggest that learning tree be supplemented by other if we are to reach artificial general intelligence. 




networking networking networking networking networking networking networking networking networking networking 
networking networking networking networking networking 
networking networking networking networking networking networking networking networking networking networking 

learning learning learning

GnuRadio GnuRadio GnuRadio GnuRadio GnuRadio
ACK ACK ACK ACK ACK ACK ACK 

 security 
 privacy 
 security 
 privacy 
       
 security 
 privacy 
 security 
 privacy 
 security 
 privacy 
 security 
 privacy 
 security 
 privacy 
 security 
 privacy 
 security 
 privacy 
 security 
 privacy    
system system
 stochastic stochastic stochastic 
blackbox blackbox blackbox blackbox blackbox
whitebox whitebox whitebox whitebox
 AQM AQM AQM AQM 
DRL DRL DRL DRL DRL 
IoT IoT IoT IoT
RL RL
RDMA RDMA
 RDMA RDMA RDMA 
 semantics  semantics  semantics  semantics  semantics  semantics  semantics 
SACK SACK SACK SACK SACK 
layering layering layering layering layering layering 
interpretability interpretability interpretability interpretability
locality locality locality locality locality locality 

P4 P4 P4 P4 P4 P4 P4 
indirection indirection indirection indirection 
controller controller controller controller controller controller 
SDN SDN SDN SDN SDN SDN SDN SDN SDN SDN SDN SDN SDN SDN SDN 
routing routing routing routing routing routing routing routing 
abstraction abstraction abstraction abstraction abstraction abstraction abstraction abstraction abstraction
mapping
convolution