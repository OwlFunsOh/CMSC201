a
    sab  �                   @   s�   d Z ddlZdZdZdZddd�Zdd	� Zd
d� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zedkr�dZe�� dvr�eeeed��� ��\ZZeee�Ze	e� ee� ed�ZqndS )z9
    Come up with a name for the game

    JMPs and HLTs
�    N�   �   �   c              
   C   s�   |rt �|� g }t| d �D ]b}t �dd�}t �d| d �}|�t jdd|� �d|� �d|� �d	|� �d
gg d�dd�d � qdg| d
g S )z�
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    �   �   �d   r   Znopzadd zsub zmul zjmp �hlt)�   r   r   r   r   r   )Zweights�k)�random�seed�range�randint�append�choices)ZlengthZthe_seedZmap_list�_Zrandom_pointsZrandom_position� r   �jmps_and_hlts.py�generate_random_map   s    
Dr   c           	         s`  t | �d }t|�|d rdnd � � fdd�t� t d �D �}t� �D �]�}|d s�t� �D ]�}|�  | t | �k r`tt|�  | ��D ](\}}||t| d  t| d | < q�t| |�  |  �D ](\}}||t| d  t| d | < q�q`qJt� d dd�D �]4}|�  | t | �k �rtt|�  | ��D ]v\}}z,||t| d  t� d |  d | < W n> t�y�   t||t| d t� d |  d | � Y n0 �q8t| |�  |  �D ]v\}}z,||t| d  t� d |  d | < W n> t�y6   t||t| d t� d |  d | � Y n0 �qĐqqJ|D ]}td�	|�� �qFd S )	N�      �?r   r   c                    sH   g | ]@}|t  r*d d� tt�  d �D �ndd� tt�  d �D ��qS )c                 S   s   g | ]}|t  rd nd�qS �� �*��
GRID_WIDTH��.0�jr   r   r   �
<listcomp>#   �    z+draw_map_new.<locals>.<listcomp>.<listcomp>r   c                 S   s   g | ]}d �qS �r   r   r   r   r   r   r   $   r   ��GRID_HEIGHTr   r   �r   �i��int_square_rootr   r   r   #   s   ��z draw_map_new.<locals>.<listcomp>r   ������ )
�len�intr   r"   �	enumerate�strr   �
IndexError�print�join)	�the_map�current_position�floating_square_root�the_display_gridr$   r   r
   �c�rowr   r%   r   �draw_map_new   s6    
�"&,4,:r6   c                    s^   | d }t |�|d rdnd � � }� � d  | kr<|d8 }� fdd�t|t d �D �}|S )z�
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    r   r   r   c                    sH   g | ]@}|t  r*d d� tt�  d �D �ndd� tt�  d �D ��qS )c                 S   s   g | ]}|t  rd nd�qS r   r   r   r   r   r   r   M   r   z(make_grid.<locals>.<listcomp>.<listcomp>r   c                 S   s   g | ]}d �qS r    r   r   r   r   r   r   N   r   r!   r#   r%   r   r   r   M   s   ��zmake_grid.<locals>.<listcomp>)r*   r   r"   )Z
table_sizer2   Ztable_heightr3   r   r%   r   �	make_gridA   s    
�r7   c                 C   s�   |d }t |�|d rdnd }|| }|| }|d dkrFt| }nt|| d  }t|�d��D ]:\}	}
t|
�D ](\}}|| t| d |	  |d | < qtqddS )aw  
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    r   r   r   r   �
N)r*   r   r+   �splitr"   )Zdisplay_grid�size�index�messager2   r&   Z	table_rowZ	table_colZcolumn_start�rZmessage_liner
   r4   r   r   r   �fill_grid_squareS   s    
r>   c                 C   sV   t t| ��}t| �D ]$\}}t|t| �||� d|� �� q|D ]}td�|�� q>d S )Nr8   r(   )r7   r)   r+   r>   r.   r/   )r0   Zthe_gridr$   �elementr5   r   r   r   �draw_mapi   s
    r@   c                 C   s�   t | �d }t|�|d rdnd }t|�D ]�}|d s�t|�D ]>}|| | t | �k rrt| || |  dd� q@tddd� q@nPt|d dd�D ]>}|| | t | �k r�t| || |  dd� q�tddd� q�t�  q,d S )	Nr   r   r   r   �	)�endr(   r'   )r)   r*   r   r.   )r0   r1   r2   r&   r$   r   r   r   r   �draw_map_oldr   s    rC   c                   C   s   t �dt�S )z,
        :return: returns the dice roll
    r   )r   r   �
DICE_SIDESr   r   r   r   �	roll_dice�   s    rE   c                 C   s�   | � � }|d dv r`t|d �}|d dkr6||7 }n*|d dkrL||8 }n|d dkr`||9 }|d dkrxt|d �}||fS )Nr   )�add�mul�subr   rF   rH   rG   Zjmp)r9   r*   )Zinstruction�scorer1   Zsplit_instruction�valuer   r   r   �execute_instruction�   s    

rK   c              	   C   s$  d}d}d}| | dkr�|t | �d k r�t� }||7 }|t | �; }td|� d|� d| | � d|� �� |}t| | ||�\}}|d7 }||kr|t | �d k r|}td|� d|� d| | � d|� �� t| | ||�\}}|d7 }q�q|t | �d k�rtd	� ntd
|� d|� d| | � �� |S )Nr   r   r   zPos: z Score: z, instruction z	 Rolled: r   z0Turn Count Exceeded, This Map Has Infinite LoopszFinal Pos: z Final Score: z, Instruction )r)   rE   r.   rK   )r0   r1   rI   ZturnsZ	dice_rollZprev_positionr   r   r   �	play_game�   s(    $$
rL   �__main__�y)�nZnozBoard Size and Seed: z
continue? )r   )�__doc__r   r   r"   rD   r   r6   r7   r>   r@   rC   rE   rK   rL   �__name__�s�lower�list�mapr*   �inputr9   Z	game_sizer   Zgame_mapr   r   r   r   �<module>   s*   
"	
