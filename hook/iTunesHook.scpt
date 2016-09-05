FasdUAS 1.101.10   ��   ��    k             l     ��  ��    8 2 This function returns true, if iTunes is running.     � 	 	 d   T h i s   f u n c t i o n   r e t u r n s   t r u e ,   i f   i T u n e s   i s   r u n n i n g .   
  
 i         I      �������� 0 itunesrunning iTunesRunning��  ��    O        E        l   	 ����  n    	    1    	��
�� 
pnam  2   ��
�� 
prcs��  ��    m   	 
   �    i T u n e s  m       �                                                                                  sevs  alis    �  Macintosh HD               �H��H+     )System Events.app                                               ���0-        ����  	                CoreServices    �H�r      ����       )   (   '  =Macintosh HD:System: Library: CoreServices: System Events.app   $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��        l     ��������  ��  ��        l     ��  ��    "  Check if iTunes is running.     �   8   C h e c k   i f   i T u n e s   i s   r u n n i n g .       l     �� ! "��   ! J D If iTunes is running, then run the itunescontroller python utility.    " � # # �   I f   i T u n e s   i s   r u n n i n g ,   t h e n   r u n   t h e   i t u n e s c o n t r o l l e r   p y t h o n   u t i l i t y .    $ % $ l     �� & '��   & U O If no face is detected, then probably the mac user is away, so pause playback.    ' � ( ( �   I f   n o   f a c e   i s   d e t e c t e d ,   t h e n   p r o b a b l y   t h e   m a c   u s e r   i s   a w a y ,   s o   p a u s e   p l a y b a c k . %  ) * ) l     �� + ,��   + { u If a face is detected, then mac user is in front of the screen, so now if the playback is paused then start playing.    , � - - �   I f   a   f a c e   i s   d e t e c t e d ,   t h e n   m a c   u s e r   i s   i n   f r o n t   o f   t h e   s c r e e n ,   s o   n o w   i f   t h e   p l a y b a c k   i s   p a u s e d   t h e n   s t a r t   p l a y i n g . *  . / . l     0���� 0 r      1 2 1 I     �������� 0 itunesrunning iTunesRunning��  ��   2 o      ���� 0 playing  ��  ��   /  3�� 3 l   Q 4���� 4 Z    Q 5 6���� 5 o    	���� 0 playing   6 k    M 7 7  8 9 8 r     : ; : I   �� <��
�� .sysoexecTEXT���     TEXT < m     = = � > >   i t u n e s c o n t r o l l e r��   ; o      ���� 0 away   9  ? @ ? l   �� A B��   A  display notification away    B � C C 2 d i s p l a y   n o t i f i c a t i o n   a w a y @  D�� D Z    M E F�� G E l    H���� H =    I J I l    K���� K c     L M L o    ���� 0 away   M m    ��
�� 
TEXT��  ��   J m     N N � O O  n o   f a c e��  ��   F O   & P Q P I    %������
�� .hookPausnull��� ��� null��  ��   Q m     R R�                                                                                  hook  alis    N  Macintosh HD               �H��H+     H
iTunes.app                                                      ���R�        ����  	                Applications    �H�r      ��/       H  %Macintosh HD:Applications: iTunes.app    
 i T u n e s . a p p    M a c i n t o s h   H D  Applications/iTunes.app   / ��  ��   G O   ) M S T S k   - L U U  V W V r   - 4 X Y X c   - 2 Z [ Z 1   - 0��
�� 
pPlS [ m   0 1��
�� 
TEXT Y o      ���� 0 playerstate playerState W  \ ] \ l  5 5�� ^ _��   ^ &  display notification playerState    _ � ` ` @ d i s p l a y   n o t i f i c a t i o n   p l a y e r S t a t e ]  a�� a Z   5 L b c���� b G   5 @ d e d =  5 8 f g f o   5 6���� 0 playerstate playerState g m   6 7 h h � i i  p a u s e d e =  ; > j k j o   ; <���� 0 playerstate playerState k m   < = l l � m m  s t o p p e d c I  C H������
�� .hookPlaynull��� ��� obj ��  ��  ��  ��  ��   T m   ) * n n�                                                                                  hook  alis    N  Macintosh HD               �H��H+     H
iTunes.app                                                      ���R�        ����  	                Applications    �H�r      ��/       H  %Macintosh HD:Applications: iTunes.app    
 i T u n e s . a p p    M a c i n t o s h   H D  Applications/iTunes.app   / ��  ��  ��  ��  ��  ��  ��       �� o p q��   o ������ 0 itunesrunning iTunesRunning
�� .aevtoappnull  �   � **** p �� ���� r s���� 0 itunesrunning iTunesRunning��  ��   r   s  ���� 
�� 
prcs
�� 
pnam�� � 	*�-�,�U q �� t���� u v��
�� .aevtoappnull  �   � **** t k     Q w w  . x x  3����  ��  ��   u   v ���� =������ N R������ h l������ 0 itunesrunning iTunesRunning�� 0 playing  
�� .sysoexecTEXT���     TEXT�� 0 away  
�� 
TEXT
�� .hookPausnull��� ��� null
�� 
pPlS�� 0 playerstate playerState
�� 
bool
�� .hookPlaynull��� ��� obj �� R*j+  E�O� F�j E�O��&�  � *j UY &� !*�,�&E�O�� 
 �� �& 
*j Y hUY h ascr  ��ޭ