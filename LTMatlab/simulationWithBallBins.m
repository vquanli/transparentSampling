function [ send_packet ] = simulationWithBallBins(packet_num,packet_length,decode_tag,receive_packet_statistic,packet_loss,SIMULATION_NUMRUNS)
%LT_LINK_SIMULATE Summary of this function goes here
%   Detailed explanation goes here


       packetNeeded=zeros((packet_num-1024)/128,SIMULATION_NUMRUNS);
       for k_n=0.5:0.25:1
        disp(k_n)
       for k=1:1:SIMULATION_NUMRUNS
           disp(k);
       for j=1024:128:(packet_num)
        
        message_matrix = randi([0 1],j,packet_length);
       
        rank_statistic = [0]; %
        H_decode = zeros(j,j);
        code_decode = zeros(j,packet_length);

        receive_packet = 0;  %
        send_packet = 0; %

    
        distribution_matrix_prob = robust_solition(j);  

        success_tag = 0;
        while(~success_tag)
        
            send_degree = randsrc(1,1,[1:size(distribution_matrix_prob,2);distribution_matrix_prob]);           
            
        
            H = zeros(1,j);
            code_encode = zeros(1,packet_length);
            message_encode_pos = [];

            
            i = 1;
            while i <= send_degree
                i = i + 1;
                temp_pos = randi(size(message_matrix,1));
                if H(temp_pos) == 0
                    H(temp_pos) = 1;
                    message_encode_pos = [message_encode_pos temp_pos];
                else
                    i = i-1;
                end
            end    

     
            for i = 1:size(message_encode_pos,2)            
                code_encode =  rem(code_encode+message_matrix(message_encode_pos(i),:),2);
            end  

       
            code_send{1,1} = code_encode; 
            code_send{1,2} = H;
            send_packet = send_packet + 1;


            %����
            

            %������·����
            packet_loss_tag = randsrc(1,1,[[0 1];[1 - packet_loss packet_loss]]);            
            if packet_loss_tag == 1
                rank_statistic = [rank_statistic rank_statistic(size(rank_statistic,2))]; 
                continue;
            end

            if decode_tag == 1
                %BP����
                receive_packet = receive_packet + 1; 
                [H_decode,code_decode,tag_decode] = LT_decode_BP_BallBins(code_send{1,2},code_send{1,1},H_decode,code_decode,j,k_n);
                rank_statistic = [rank_statistic find_rank(H_decode)];
            elseif decode_tag == 2
                %��˹����
                receive_packet = receive_packet + 1; 
                [H_decode,code_decode,tag_decode,rank_statistic] = LT_decode_GuassianBallBins(code_send{1,2},code_send{1,1},H_decode,code_decode,rank_statistic,j,k_n); 
            end

            if tag_decode == 1                       
                % disp('decode success');
                % disp('receive packet num is');
                % disp(receive_packet);
                % disp('send packet num is');
                % disp(send_packet);
%                 if decode_tag == 1
%                     %BP����
%                 elseif decode_tag == 2
%                     %��˹����
%                   %  receive_packet_statistic = [receive_packet_statistic receive_packet];
%                 end
% 
%                 send_bit_total = receive_packet * packet_length;
                 success_tag = 1;
%                 plot(rank_statistic / packet_num)  %������ͼ��
                packetNeeded((j-896)/128,k)= receive_packet;
                break;
            end 
        end 

       end
       end
       disp(packetNeeded);
        packetNeededVar=[];
       
       packetNeededVar=mean(packetNeeded, 2);
       
       disp(packetNeededVar)
       x=1024:128:packet_num;
       plot(x,packetNeededVar,'o-');
        
       end

end
